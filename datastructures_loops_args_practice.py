"""
Python Practice Assignment: Data Structures, Loops & Function Arguments
========================================================================
Instructions:
  - Each function below has a TODO describing what it must do.
  - Replace the `pass` (and any ___ placeholders) with your own code.
  - Do not change function names or parameter names — the checks at the
    bottom of the file depend on them.
  - Run this file directly to see whether your answers match the
    expected output:  python datastructures_loops_args_practice.py
"""


# ---------------------------------------------------------------------------
# Section 1: Lists
# ---------------------------------------------------------------------------

# Question 1
def make_list_demo():
    """
    TODO: Create a list called `numbers` containing 1, 2, 3, 4, 5 and
    return it.
    """
    pass
def make_list_demo():
    numbers = [1, 2, 3, 4, 5]
    return numbers

# Question 2
def sum_list(numbers):
    """
    TODO: Return the sum of all numbers in the list `numbers` using a
    for loop (do not use the built-in sum()).
    Example: sum_list([1, 2, 3, 4]) -> 10
    """
    pass
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# Question 3
def double_values(numbers):
    """
    TODO: Return a NEW list where every value in `numbers` is doubled,
    using a list comprehension.
    Example: double_values([1, 2, 3]) -> [2, 4, 6]
    """
    pass
def double_values(numbers):
    return [n * 2 for n in numbers]


# Question 4
def evens_only(numbers):
    """
    TODO: Return a list containing only the even numbers from `numbers`,
    using a list comprehension with a condition.
    Example: evens_only([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
    """
    pass
def evens_only(numbers):
    return [number for number in numbers if number % 2 == 0]


# Question 5
def reverse_list(items):
    """
    TODO: Return `items` reversed, using slicing (not .reverse() or
    reversed()).
    Example: reverse_list([1, 2, 3]) -> [3, 2, 1]
    """
    pass
def reverse_list(items):
    return items[::-1]

# ---------------------------------------------------------------------------
# Section 2: Tuples & Sets
# ---------------------------------------------------------------------------

# Question 6
def make_point():
    """
    TODO: Create a tuple called `point` with the values (3, 7) and
    return it.
    """
    pass
def make_point():
    point = (3, 7)
    return point


# Question 7
def unpack_point(point):
    """
    TODO: `point` is a tuple like (3, 7). Unpack it into variables
    `x` and `y` in one line, then return the string "x=<x>, y=<y>".
    Example: unpack_point((3, 7)) -> "x=3, y=7"
    """
    pass
def unpack_point(point):
    x, y = point
    return f"x={x}, y={y}"


# Question 8
def unique_values(items):
    """
    TODO: Given a list `items` that may contain duplicates, return a
    set containing only the unique values.
    Example: unique_values([1, 2, 2, 3, 1]) -> {1, 2, 3}
    """
    pass
def unique_values(items):
    return set(items)


# ---------------------------------------------------------------------------
# Section 3: Dictionaries
# ---------------------------------------------------------------------------

# Question 9
def make_student_record():
    """
    TODO: Create a dictionary called `student` with keys "name" (value
    "Omar") and "grade" (value 90). Return it.
    """
    pass
def make_student_record():
    student = {
        "name": "Omar",
        "grade": 90
    }
    return student



# Question 10
def get_grade(student):
    """
    TODO: `student` is a dict with a "grade" key. Return its value.
    Example: get_grade({"name": "Omar", "grade": 90}) -> 90
    """
    pass
def get_grade(student):
    return student["grade"]


# Question 11
def add_key(dictionary, key, value):
    """
    TODO: Add `key` with `value` to `dictionary` and return the updated
    dictionary.
    Example: add_key({"a": 1}, "b", 2) -> {"a": 1, "b": 2}
    """
    pass
def add_key(dictionary, key, value):
    dictionary[key] = value
    return dictionary


# Question 12
def dict_keys_as_list(dictionary):
    """
    TODO: Return a list of all the keys in `dictionary`.
    Example: dict_keys_as_list({"a": 1, "b": 2}) -> ["a", "b"]
    """
    pass
def dict_keys_as_list(dictionary):
    return list(dictionary.keys())


# Question 13
def sum_dict_values(scores):
    """
    TODO: `scores` is a dict of name -> score. Loop over the dict's
    values and return their total.
    Example: sum_dict_values({"Ana": 10, "Sam": 5}) -> 15
    """
    pass
def sum_dict_values(scores):
    total = 0
    for score in scores.values():
        total += score
    return total

# ---------------------------------------------------------------------------
# Section 4: Loops
# ---------------------------------------------------------------------------

# Question 14
def countdown(n):
    """
    TODO: Using a while loop, return a list counting down from `n` to 1
    (inclusive), in that order.
    Example: countdown(5) -> [5, 4, 3, 2, 1]
    """
    pass
def countdown(n):
    result = []

    while n >= 1:
        result.append(n)
        n -= 1

    return result

# Question 15
def find_first_negative(numbers):
    """
    TODO: Loop through `numbers` and return the first negative number
    found. Use `break` once you find it. If none are negative, return
    None.
    Example: find_first_negative([3, 5, -2, 8]) -> -2
    """
    pass
def find_first_negative(numbers):
    for number in numbers:
        if number < 0:
            return number
            break

    return None


# Question 16
def count_vowels(word):
    """
    TODO: Loop through each character in `word` and count how many are
    vowels (a, e, i, o, u — lowercase only). Use `continue` to skip
    non-vowel characters. Return the count.
    Example: count_vowels("banana") -> 3
    """
    pass
def count_vowels(word):
    count = 0

    for letter in word:
        if letter not in "aeiou":
            continue

        count += 1

    return count


# Question 17
def multiplication_table(n):
    """
    TODO: Using a nested for loop, return a list of strings showing the
    multiplication table of `n` from 1 to 3.
    Example: multiplication_table(2) -> ["2 x 1 = 2", "2 x 2 = 4", "2 x 3 = 6"]
    """
    pass
def multiplication_table(n):
    result = []

    for i in range(1, 4):
        result.append(f"{n} x {i} = {n * i}")

    return result


# ---------------------------------------------------------------------------
# Section 5: Function Arguments — positional, keyword, default, *args, **kwargs
# ---------------------------------------------------------------------------

# Question 18
def describe_pet(name, animal_type="dog"):
    """
    TODO: Return "<name> is a <animal_type>". `animal_type` should have
    a default value of "dog" so it can be called with just a name.
    Example: describe_pet("Rex") -> "Rex is a dog"
    Example: describe_pet("Whiskers", animal_type="cat") -> "Whiskers is a cat"
    """
    pass
def describe_pet(name, animal_type="dog"):
    return f"{name} is a {animal_type}"


# Question 19
def add_all(*args):
    """
    TODO: Accept any number of positional arguments using *args and
    return their sum.
    Example: add_all(1, 2, 3) -> 6
    Example: add_all(5) -> 5
    Example: add_all() -> 0
    """
    pass
def add_all(*args):
    total = 0

    for number in args:
        total += number

    return total

# Question 20
def build_profile(**kwargs):
    """
    TODO: Accept any number of keyword arguments using **kwargs and
    return them as a dictionary (kwargs already behaves like one — just
    return it).
    Example: build_profile(name="Lina", age=22) -> {"name": "Lina", "age": 22}
    """
    pass
def build_profile(**kwargs):
    return kwargs


# Question 21
def order_summary(item, qty, *extras, discount=0, **notes):
    """
    TODO: This combines positional args (item, qty), an arbitrary
    positional collector (*extras), a keyword-only arg with a default
    (discount), and an arbitrary keyword collector (**notes).
    Return a dictionary with keys:
      "item"     -> the item value
      "qty"      -> the qty value
      "extras"   -> a list of the extra positional args
      "discount" -> the discount value
      "notes"    -> the notes dict
    Example: order_summary("pen", 3, "gift-wrap", discount=10, note="rush")
             -> {"item": "pen", "qty": 3, "extras": ["gift-wrap"],
                 "discount": 10, "notes": {"note": "rush"}}
    """
    pass
def order_summary(item, qty, *extras, discount=0, **notes):
    return {
        "item": item,
        "qty": qty,
        "extras": list(extras),
        "discount": discount,
        "notes": notes
    }

# ---------------------------------------------------------------------------
# Self-check harness — run this file to see which answers are correct.
# Do not edit below this line.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    checks = [
        (make_list_demo, (), [1, 2, 3, 4, 5]),
        (sum_list, ([1, 2, 3, 4],), 10),
        (double_values, ([1, 2, 3],), [2, 4, 6]),
        (evens_only, ([1, 2, 3, 4, 5, 6],), [2, 4, 6]),
        (reverse_list, ([1, 2, 3],), [3, 2, 1]),
        (make_point, (), (3, 7)),
        (unpack_point, ((3, 7),), "x=3, y=7"),
        (unique_values, ([1, 2, 2, 3, 1],), {1, 2, 3}),
        (make_student_record, (), {"name": "Omar", "grade": 90}),
        (get_grade, ({"name": "Omar", "grade": 90},), 90),
        (add_key, ({"a": 1}, "b", 2), {"a": 1, "b": 2}),
        (dict_keys_as_list, ({"a": 1, "b": 2},), ["a", "b"]),
        (sum_dict_values, ({"Ana": 10, "Sam": 5},), 15),
        (countdown, (5,), [5, 4, 3, 2, 1]),
        (find_first_negative, ([3, 5, -2, 8],), -2),
        (count_vowels, ("banana",), 3),
        (multiplication_table, (2,), ["2 x 1 = 2", "2 x 2 = 4", "2 x 3 = 6"]),
        (describe_pet, ("Rex",), "Rex is a dog"),
        (add_all, (1, 2, 3), 6),
        (build_profile, (), {}),
        (
            order_summary,
            ("pen", 3, "gift-wrap"),
            {"item": "pen", "qty": 3, "extras": ["gift-wrap"],
             "discount": 0, "notes": {}},
        ),
    ]

    passed = 0
    for i, (func, args, expected) in enumerate(checks, start=1):
        try:
            result = func(*args)
            ok = result == expected
        except Exception as e:
            result = f"ERROR: {e}"
            ok = False
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Q{i:>2} [{status}] {func.__name__}{args} -> {result!r} (expected {expected!r})")

    # Extra manual checks for keyword-heavy functions (not easily table-driven)
    extra_checks = [
        ("describe_pet keyword default override",
         describe_pet("Whiskers", animal_type="cat"), "Whiskers is a cat"),
        ("build_profile with kwargs",
         build_profile(name="Lina", age=22), {"name": "Lina", "age": 22}),
        ("order_summary with discount and notes",
         order_summary("pen", 3, "gift-wrap", discount=10, note="rush"),
         {"item": "pen", "qty": 3, "extras": ["gift-wrap"],
          "discount": 10, "notes": {"note": "rush"}}),
    ]
    print("\n--- Extra checks ---")
    for label, result, expected in extra_checks:
        try:
            ok = result == expected
        except Exception as e:
            result = f"ERROR: {e}"
            ok = False
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"[{status}] {label} -> {result!r} (expected {expected!r})")

    total = len(checks) + len(extra_checks)
    print(f"\n{passed}/{total} questions passed.")
