# 🚇 Metro Ticket Booking — حجز تذاكر المترو

Arabic (RTL) web app for booking Cairo Metro Line 1 tickets, built with **Python, Streamlit, SQLite and Pandas**.

تطبيق ويب بالعربي لحجز تذاكر مترو القاهرة (الخط الأول).

## المميزات
- حجز تذكرة باختيار محطة القيام والوصول
- حساب السعر تلقائيًا حسب المسافة ونوع التذكرة (عادي / طالب / مسن)
- رقم حجز فريد لكل عملية
- الاستعلام عن الحجز برقم الموبايل أو رقم الحجز
- لوحة تحكم محمية بكلمة سر

## التشغيل
```bash
pip install -r requirements.txt
streamlit run metro_app.py
```

## تفعيل لوحة التحكم
انسخ `.streamlit/secrets.toml.example` إلى `.streamlit/secrets.toml` وغيّر `ADMIN_PASSWORD`.
(الملف ده مستثنى من GitHub في `.gitignore`.)

## ملاحظات
- التسعير: `5 جنيه + 1 جنيه لكل 5 محطات`، وتقدر تعدّله من `BASE_PRICE` و`STATIONS_PER_EXTRA_POUND` فوق الملف.
- قاعدة البيانات `metro.db` بتتعمل تلقائيًا أول تشغيل.
