"""
Python Practice Assignment: Variables & Strings
================================================
Instructions:
  - Each function below has a TODO describing what it must do.
  - Replace the `pass` (and any ___ placeholders) with your own code.
  - Do not change function names or parameter names — the checks at the
    bottom of the file depend on them.
  - Run this file directly to see whether your answers match the
    expected output:  python variables_and_strings_practice.py
"""


# Question 1
def build_greeting(name, age):
    """
    TODO: Return the string "My name is <name> and I am <age> years old"
    using string concatenation. Convert age to a string before joining.
    Example: build_greeting("Layla", 21) -> "My name is Layla and I am 21 years old"
    """
    pass
def build_greeting(name, age):
    return "My name is " + name + " and I am " + str(age) + " years old"



# Question 2
def make_valid_variable_demo():
    """
    TODO: Create a variable named `_total_count` and assign it the value 100.
    Return the variable's value.
    (This question checks that you understand valid Python variable naming.)
    """
    pass
def make_valid_variable_demo():
    _total_count = 100
    return _total_count

# Question 3
def add_as_strings(a, b):
    """
    TODO: Given two values, convert both to strings and concatenate them
    with "+" (not add them numerically).
    Example: add_as_strings(5, 5) -> "55"
    Example: add_as_strings(2, 3) -> "23"
    """
    pass
def add_as_strings(a, b):
    return str(a) + str(b)


# Question 4
def format_order_number(order_number):
    """
    TODO: Return "Order #<order_number> is ready for pickup".
    order_number will be an integer — convert it to a string first.
    Example: format_order_number(4521) -> "Order #4521 is ready for pickup"
    """
    pass
def format_order_number(order_number):
    return "Order #" + str(order_number) + " is ready for pickup"


# Question 5
def weather_report(city, temp):
    """
    TODO: Using an f-string, return "The temperature in <city> is <temp> degrees".
    Example: weather_report("Cairo", 34) -> "The temperature in Cairo is 34 degrees"
    """
    pass
def weather_report(city, temp):
    return f"The temperature in {city} is {temp} degrees"

# Question 6
def first_and_last_char(word):
    """
    TODO: Return a string containing the first character and the last
    character of `word`, in that order, using indexing.
    Example: first_and_last_char("python") -> "pn"
    """
    pass
def first_and_last_char(word):
    return word[0] + word[-1]

# Question 7
def get_second_word(phrase):
    """
    TODO: `phrase` is "hello world". Using slicing (not split), return
    everything from index 6 onward.
    Example: get_second_word("hello world") -> "world"
    """
    pass
def get_second_word(phrase):
    return phrase[6:]

# Question 8
def every_other_letter(letters):
    """
    TODO: Using slicing with a step, return every other character in
    `letters`, starting from the first one.
    Example: every_other_letter("abcdefgh") -> "aceg"
    """
    pass
def every_other_letter(letters):
    return letters[::2]

# Question 9
def username_length(username):
    """
    TODO: Return the number of characters in `username` as an integer.
    Example: username_length("coder_2024") -> 10
    """
    pass
def username_length(username):
    return len(username)


# Question 10
def shout(title):
    """
    TODO: Return `title` converted entirely to uppercase.
    Example: shout("Introduction to Python") -> "INTRODUCTION TO PYTHON"
    """
    pass
def shout(title):
    return title.upper()


# Question 11
def swap_word(sentence, old_word, new_word):
    """
    TODO: Return `sentence` with every occurrence of `old_word` replaced
    by `new_word`.
    Example: swap_word("I like cats", "cats", "dogs") -> "I like dogs"
    """
    pass
def swap_word(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)

# Question 12
def clean_input(raw_input):
    """
    TODO: Return `raw_input` with leading and trailing whitespace removed.
    Example: clean_input("   welcome   ") -> "welcome"
    """
    pass
def clean_input(raw_input):
    return raw_input.strip()

# Question 13
def split_into_words(sentence):
    """
    TODO: Split `sentence` on spaces and return the resulting list of words.
    Example: split_into_words("the quick brown fox")
             -> ["the", "quick", "brown", "fox"]
    """
    pass
def split_into_words(sentence):
    return sentence.split(" ")

def countdown(n):
    result = []

    while n >= 1:
        result.append(n)
        n -= 1

    return result

# Question 14
def join_with_dashes(words):
    """
    TODO: Join the list `words` into a single string separated by dashes.
    Example: join_with_dashes(["red", "green", "blue"]) -> "red-green-blue"
    """
    pass
def join_with_dashes(words):
    return "-".join(words)

# Question 15
def total_from_text(price_text):
    """
    TODO: `price_text` is a string like "45". Convert it to an integer,
    then return the string "Total: <price>".
    Example: total_from_text("45") -> "Total: 45"
    """
    pass
def total_from_text(price_text):
    price = int(price_text)
    return "Total: " + str(price)

# Question 16
def quote_line():
    """
    TODO: Return the exact two-line string below using escape characters
    for the quotation marks and the line break:

        She said, "Python is fun!"
        Let's learn it.
    """
    pass
def total_from_text(price_text):
    price = int(price_text)
    return "Total: " + str(price)

# Question 17
def uppercase_first_letter(word):
    """
    TODO: Strings are immutable, so you can't do word[0] = "X".
    Instead, return a NEW string with the first letter of `word`
    capitalized, using slicing/concatenation (not word.capitalize()).
    Example: uppercase_first_letter("cat") -> "Cat"
    """
    pass
def uppercase_first_letter(word):
    return word[0].upper() + word[1:]


# Question 18
def combine_colors():
    """
    TODO: Using multiple assignment on one line, assign "red", "green",
    and "blue" to variables a, b, c respectively. Return the string
    "<b> and <c>".
    Example: combine_colors() -> "green and blue"
    """
    pass
def combine_colors():
    a, b, c = "red", "green", "blue"
    return f"{b} and {c}"


# Question 19
def format_receipt(item, price):
    """
    TODO: Return "<item>: $<price>". Convert price to a string.
    Example: format_receipt("Coffee", 4.5) -> "Coffee: $4.5"
    Example: format_receipt("Bagel", 3) -> "Bagel: $3"
    """
    pass
def format_receipt(item, price):
    return item + ": $" + str(price)


# Question 20
def loud_full_name(first_name, last_name):
    """
    TODO: Combine first_name and last_name with a space between them,
    convert the result to uppercase, and return it inside a greeting
    using an f-string: "Hello, <FULL NAME>!"
    Example: loud_full_name("Ana", "Ruiz") -> "Hello, ANA RUIZ!"
    """
    pass
def loud_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    full_name = full_name.upper()
    return f"Hello, {full_name}!"


# ---------------------------------------------------------------------------
# Self-check harness — run this file to see which answers are correct.
# Do not edit below this line.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    checks = [
        (build_greeting, ("Layla", 21), "My name is Layla and I am 21 years old"),
        (make_valid_variable_demo, (), 100),
        (add_as_strings, (5, 5), "55"),
        (format_order_number, (4521,), "Order #4521 is ready for pickup"),
        (weather_report, ("Cairo", 34), "The temperature in Cairo is 34 degrees"),
        (first_and_last_char, ("python",), "pn"),
        (get_second_word, ("hello world",), "world"),
        (every_other_letter, ("abcdefgh",), "aceg"),
        (username_length, ("coder_2024",), 10),
        (shout, ("Introduction to Python",), "INTRODUCTION TO PYTHON"),
        (swap_word, ("I like cats", "cats", "dogs"), "I like dogs"),
        (clean_input, ("   welcome   ",), "welcome"),
        (split_into_words, ("the quick brown fox",), ["the", "quick", "brown", "fox"]),
        (join_with_dashes, (["red", "green", "blue"],), "red-green-blue"),
        (total_from_text, ("45",), "Total: 45"),
        (quote_line, (), "She said, \"Python is fun!\"\nLet's learn it."),
        (uppercase_first_letter, ("cat",), "Cat"),
        (combine_colors, (), "green and blue"),
        (format_receipt, ("Coffee", 4.5), "Coffee: $4.5"),
        (loud_full_name, ("Ana", "Ruiz"), "Hello, ANA RUIZ!"),
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

    print(f"\n{passed}/{len(checks)} questions passed.")
