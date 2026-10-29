
"""
Regular Expressions (RegEx)
Topics:
1. Search for a pattern
2. Find all numbers
3. Validate a 10-digit format
4. Replace text
5. Split text
"""

import re


def find_python_words(text):
    """Find every occurrence of Python, ignoring case."""
    return re.findall(r"Python", text, flags=re.IGNORECASE)


def extract_numbers(text):
    """Extract all consecutive groups of digits."""
    return re.findall(r"\d+", text)


def validate_phone_format(phone):
    """Check whether the input contains exactly 10 digits."""
    return re.fullmatch(r"\d{10}", phone) is not None


def hide_numbers(text):
    """Replace each consecutive group of digits with asterisks."""
    return re.sub(r"\d+", "*", text)


def split_words(text):
    """Split text wherever one or more spaces occur."""
    return re.split(r"\s+", text.strip())


def main():
    text = "Python is useful. I practice Python for 2 hours."

    print("1. Find Python words:")
    print(find_python_words(text))

    print("\n2. Extract numbers:")
    print(extract_numbers(text))

    print("\n3. Validate phone format:")
    phone = input("Enter a 10-digit phone number: ")
    if validate_phone_format(phone):
        print("Valid format")
    else:
        print("Invalid format")

    print("\n4. Hide numbers:")
    print(hide_numbers(text))

    print("\n5. Split words:")
    print(split_words("Learn   Python   every day"))


if __name__ == "__main__":
    main()
