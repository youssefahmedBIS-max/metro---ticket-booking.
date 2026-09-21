# -*- coding: utf-8 -*-
"""
مشروع حجز تذاكر مترو القاهرة (الخط الأول)
التقنيات: Python + Streamlit + SQLite + Pandas
التشغيل:  streamlit run metro_app.py
"""

import hmac
import html
import os
import re
import secrets
import sqlite3
import string
from contextlib import closing
from datetime import datetime

import pandas as pd
import streamlit as st

# ==========================================
# إعدادات الصفحة (لازم تكون أول أمر Streamlit)
# ==========================================
st.set_page_config(
    page_title="حجز تذاكر المترو",
    page_icon="🚇",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# تنسيق CSS للعربية (RTL)
# ==========================================
st.markdown(
    """
<style>
    .stApp, [data-testid="stSidebar"] {
        direction: rtl;
        text-align: right;
    }
    .stButton>button, .stFormSubmitButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #0066cc;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover, .stFormSubmitButton>button:hover {
        background-color: #004999;
        color: white;
    }
    h1, h2, h3 {
        color: #004999;
        text-align: right;
    }
    .ticket-box {
        background-color: #f0f8ff;
        color: #1a1a1a;
        padding: 20px;
        border-radius: 12px;
        border-right: 6px solid #0066cc;
        margin-top: 15px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# الإعدادات العامة
# ==========================================
# مكان قاعدة البيانات: جنب الملف ده بالظبط، مهما شغّلت التطبيق من أي فولدر
DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "metro.db")

# محطات الخط الأول (حلوان ← المرج الجديدة) بالترتيب الحقيقي من الجنوب للشمال
ALL_STATIONS = [
    "حلوان", "عين حلوان", "جامعة حلوان", "وادي حوف", "حدائق حلوان",
    "المعصرة", "طرة الأسمنت", "كوتسيكا", "طرة البلد", "ثكنات المعادي",
    "المعادي", "حدائق المعادي", "دار السلام", "الزهراء", "مار جرجس",
    "الملك الصالح", "السيدة زينب", "سعد زغلول", "السادات", "ناصر",
    "عرابي", "الشهداء", "غمرة", "الدمرداش", "منشية الصدر",
    "كوبري القبة", "حمامات القبة", "سراي القبة", "حدائق الزيتون", "حلمية الزيتون",
    "المطرية", "عين شمس", "عزبة النخل", "المرج", "المرج الجديدة",
]

# معامل السعر لكل نوع تذكرة (1.0 = السعر كامل، 0.5 = نص السعر، 0.25 = ربع السعر)
TICKET_MULTIPLIERS = {
    "عادي": 1.0,
    "طالب": 0.5,
    "مسن": 0.25,
}

# قاعدة التسعير: السعر الأساسي + جنيه لكل كام محطة
BASE_PRICE = 5
STATIONS_PER_EXTRA_POUND = 5

# أسماء الأعمدة اللي بتظهر في لوحة التحكم
COLUMN_NAMES_AR = {
    "id": "م",
    "booking_ref": "رقم الحجز",
    "name": "الاسم",
    "phone": "الموبايل",
    "from_station": "من",
    "to_station": "إلى",
    "ticket_type": "نوع التذكرة",
    "count": "العدد",
    "total": "الإجمالي",
    "booking_date": "تاريخ الحجز",
}

# ==========================================
# قاعدة البيانات
# ==========================================
def get_connection():
    """فتح اتصال جديد بقاعدة البيانات"""
    return sqlite3.connect(DB_NAME)


def init_db():
    """إنشاء جدول الحجوزات إذا لم يكن موجودًا"""
    # closing = يقفل الاتصال في الآخر  |  with conn = يعمل commit (أو rollback لو حصل خطأ)
    with closing(get_connection()) as conn, conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_ref TEXT UNIQUE,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                from_station TEXT NOT NULL,
                to_station TEXT NOT NULL,
                ticket_type TEXT NOT NULL,
                count INTEGER NOT NULL,
                total REAL NOT NULL,
                booking_date TEXT NOT NULL
            )
            """
        )


def add_booking(booking_data):
    """إضافة حجز جديد لقاعدة البيانات"""
    with closing(get_connection()) as conn, conn:
        conn.execute(
            """
            INSERT INTO bookings
            (booking_ref, name, phone, from_station, to_station,
             ticket_type, count, total, booking_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                booking_data["booking_ref"],
                booking_data["name"],
                booking_data["phone"],
                booking_data["from_station"],
                booking_data["to_station"],
                booking_data["ticket_type"],
                booking_data["count"],
                booking_data["total"],
                booking_data["booking_date"],
            ),
        )


def get_bookings(phone=None, ref=None):
    """استرجاع الحجوزات حسب رقم الموبايل أو رقم الحجز"""
    query = "SELECT * FROM bookings"
    params = []
    if phone:
        query += " WHERE phone = ?"
        params.append(phone)
    elif ref:
        query += " WHERE booking_ref = ?"
        params.append(ref)
    query += " ORDER BY booking_date DESC"
    with closing(get_connection()) as conn:
        return pd.read_sql_query(query, conn, params=params)


def get_all_bookings():
    """استرجاع كل الحجوزات"""
    return get_bookings()


# ==========================================
# دوال مساعدة
# ==========================================
def generate_booking_ref():
    """توليد رقم حجز عشوائي (مثال: METRO-KQZ4821)"""
    letters = "".join(secrets.choice(string.ascii_uppercase) for _ in range(3))
    numbers = "".join(secrets.choice(string.digits) for _ in range(4))
    return f"METRO-{letters}{numbers}"


def calculate_price(from_station, to_station, ticket_type, count):
    """حساب السعر حسب المسافة (عدد المحطات) ونوع التذكرة"""
    if from_station not in ALL_STATIONS or to_station not in ALL_STATIONS:
        return 0
    distance = abs(ALL_STATIONS.index(from_station) - ALL_STATIONS.index(to_station))
    base_price = BASE_PRICE + distance // STATIONS_PER_EXTRA_POUND
    multiplier = TICKET_MULTIPLIERS.get(ticket_type, 1.0)
    return round(base_price * multiplier * count, 2)


# الأرقام العربية (٠١٢...) ← أرقام إنجليزي، عشان اللي بيكتب من كيبورد عربي
ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
PHONE_PATTERN = re.compile(r"01[0125][0-9]{8}")  # 010 / 011 / 012 / 015 + 8 أرقام


def normalize_phone(phone):
    """تنضيف رقم الموبايل: شيل المسافات وحوّل الأرقام العربية"""
    return phone.strip().translate(ARABIC_DIGITS)


def is_valid_phone(phone):
    """رقم موبايل مصري صحيح؟ (11 رقم ويبدأ بـ 010/011/012/015)"""
    return PHONE_PATTERN.fullmatch(phone) is not None


def create_booking(name, phone, from_station, to_station, ticket_type, count):
    """حساب السعر + توليد رقم حجز + الحفظ. ترجّع بيانات الحجز."""
    total = calculate_price(from_station, to_station, ticket_type, count)
    booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # لو رقم الحجز اتكرر صدفة (نادر جدًا) نجرّب رقم تاني
    for _ in range(5):
        booking_data = {
            "booking_ref": generate_booking_ref(),
            "name": name,
            "phone": phone,
            "from_station": from_station,
            "to_station": to_station,
            "ticket_type": ticket_type,
            "count": count,
            "total": total,
            "booking_date": booking_date,
        }
        try:
            add_booking(booking_data)
            return booking_data
        except sqlite3.IntegrityError:
            continue
    raise RuntimeError("تعذّر توليد رقم حجز فريد، حاول مرة أخرى.")


def get_admin_password():
    """كلمة سر لوحة التحكم: من secrets بتاع Streamlit أو من متغير بيئة. مفيش قيمة افتراضية."""
    try:
        password = st.secrets.get("ADMIN_PASSWORD")
    except Exception:  # مفيش ملف secrets.toml
        password = None
    return password or os.environ.get("ADMIN_PASSWORD")


# ==========================================
# تهيئة قاعدة البيانات
# ==========================================
init_db()

# ==========================================
# واجهة التطبيق
# ==========================================
st.sidebar.title("🚇 مترو الأنفاق")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "اختر الخدمة:",
    ["🎫 حجز تذكرة", "🔍 استعلام عن حجز", "📋 كل الحجوزات", "ℹ️ عن المشروع"],
)

# ---------- صفحة حجز تذكرة ----------
if menu == "🎫 حجز تذكرة":
    st.title("🎫 حجز تذكرة مترو")
    st.markdown("يرجى ملء البيانات التالية لحجز تذكرتك:")

    with st.form("booking_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("الاسم بالكامل", placeholder="مثال: أحمد محمد", max_chars=60)
            phone = st.text_input("رقم الموبايل", placeholder="01xxxxxxxxx", max_chars=11)
            from_station = st.selectbox("محطة القيام", ALL_STATIONS)
        with col2:
            to_station = st.selectbox("محطة الوصول", ALL_STATIONS, index=1)
            ticket_type = st.selectbox("نوع التذكرة", list(TICKET_MULTIPLIERS.keys()))
            count = st.number_input("عدد التذاكر", min_value=1, max_value=10, value=1, step=1)

        submitted = st.form_submit_button("احجز الآن")

    if submitted:
        name = name.strip()
        phone = normalize_phone(phone)

        # التحقق من البيانات
        if not name:
            st.error("⚠️ من فضلك أدخل الاسم.")
        elif not is_valid_phone(phone):
            st.error("⚠️ رقم الموبايل غير صحيح. لازم يكون 11 رقم ويبدأ بـ 010 أو 011 أو 012 أو 015.")
        elif from_station == to_station:
            st.error("⚠️ لا يمكن أن تكون محطة القيام هي نفسها محطة الوصول.")
        else:
            try:
                booking = create_booking(
                    name, phone, from_station, to_station, ticket_type, int(count)
                )
            except Exception:
                st.error("❌ حدث خطأ أثناء الحجز. حاول مرة أخرى.")
            else:
                st.balloons()
                st.success("✅ تم الحجز بنجاح!")

                # html.escape: عشان لو حد كتب كود HTML في الاسم ما يتنفذش في الصفحة
                safe = {key: html.escape(str(value)) for key, value in booking.items()}
                st.markdown(
                    f"""
                    <div class="ticket-box">
                        <h3>🎟️ تفاصيل التذكرة</h3>
                        <p><strong>رقم الحجز:</strong> {safe['booking_ref']}</p>
                        <p><strong>الاسم:</strong> {safe['name']}</p>
                        <p><strong>الموبايل:</strong> {safe['phone']}</p>
                        <p><strong>من:</strong> {safe['from_station']} ← <strong>إلى:</strong> {safe['to_station']}</p>
                        <p><strong>نوع التذكرة:</strong> {safe['ticket_type']}</p>
                        <p><strong>عدد التذاكر:</strong> {safe['count']}</p>
                        <p><strong>الإجمالي:</strong> {safe['total']} جنيه</p>
                        <p><strong>تاريخ الحجز:</strong> {safe['booking_date']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.info("💡 يمكنك الاستعلام عن الحجز لاحقًا باستخدام رقم الموبايل أو رقم الحجز.")

# ---------- صفحة استعلام ----------
elif menu == "🔍 استعلام عن حجز":
    st.title("🔍 الاستعلام عن حجز")
    st.markdown("ابحث باستخدام رقم الموبايل أو رقم الحجز.")

    search_type = st.radio("طريقة البحث:", ["رقم الموبايل", "رقم الحجز"], horizontal=True)
    search_value = st.text_input("أدخل القيمة:")

    if st.button("بحث"):
        value = search_value.strip()
        if not value:
            st.warning("⚠️ من فضلك أدخل قيمة للبحث.")
        else:
            if search_type == "رقم الموبايل":
                df = get_bookings(phone=normalize_phone(value))
            else:
                df = get_bookings(ref=value.upper())

            if df.empty:
                st.warning("❌ لا توجد حجوزات مطابقة.")
            else:
                st.success(f"✅ تم العثور على {len(df)} حجز.")
                for _, row in df.iterrows():
                    with st.expander(
                        f"🎫 {row['booking_ref']} - {row['from_station']} → {row['to_station']}"
                    ):
                        st.write(f"**الاسم:** {row['name']}")
                        st.write(f"**الموبايل:** {row['phone']}")
                        st.write(f"**نوع التذكرة:** {row['ticket_type']}")
                        st.write(f"**عدد التذاكر:** {row['count']}")
                        st.write(f"**الإجمالي:** {row['total']} جنيه")
                        st.write(f"**تاريخ الحجز:** {row['booking_date']}")

# ---------- صفحة كل الحجوزات (محمية بكلمة سر) ----------
elif menu == "📋 كل الحجوزات":
    st.title("📋 لوحة التحكم - كل الحجوزات")
    admin_password = get_admin_password()

    if not admin_password:
        st.warning(
            "لوحة التحكم مقفولة لأن كلمة السر لسه متضبطتش. "
            "اعمل ملف `.streamlit/secrets.toml` واكتب فيه: `ADMIN_PASSWORD = \"كلمة-سر-قوية\"` "
            "ثم أعد تشغيل التطبيق."
        )
    else:
        password = st.text_input("أدخل كلمة المرور:", type="password")
        if password and hmac.compare_digest(password.encode(), admin_password.encode()):
            df = get_all_bookings()
            if df.empty:
                st.info("لا توجد حجوزات حتى الآن.")
            else:
                st.dataframe(df.rename(columns=COLUMN_NAMES_AR))
                st.metric("إجمالي الحجوزات", len(df))
                st.metric("إجمالي الإيرادات", f"{df['total'].sum():.2f} جنيه")
        elif password:
            st.error("❌ كلمة المرور غير صحيحة.")

# ---------- صفحة عن المشروع ----------
else:
    st.title("ℹ️ عن المشروع")
    st.markdown(
        """
    ### مشروع حجز تذاكر مترو الأنفاق 🚇

    **التقنيات المستخدمة:**
    - Python
    - Streamlit (لواجهة المستخدم)
    - SQLite (قاعدة البيانات)
    - Pandas (لعرض البيانات)

    **المميزات:**
    - حجز تذكرة مع اختيار محطة القيام والوصول (محطات الخط الأول).
    - حساب السعر تلقائيًا حسب المسافة ونوع التذكرة.
    - دعم أنواع تذاكر: عادي، طالب، مسن.
    - توليد رقم حجز فريد لكل عملية.
    - استعلام عن الحجز برقم الموبايل أو رقم الحجز.
    - لوحة تحكم محمية بكلمة سر لعرض جميع الحجوزات.

    **طريقة التشغيل:**
    1. ثبّت المكتبات: `pip install -r requirements.txt`
    2. شغّل التطبيق: `streamlit run metro_app.py`
    """
    )
