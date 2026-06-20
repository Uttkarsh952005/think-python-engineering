"""
Chapter 6: Exercises
Working with recursion that returns values, and string manipulations.
"""


def first(word: str) -> str:
    return word[0]


def last(word: str) -> str:
    return word[-1]


def middle(word: str) -> str:
    return word[1:-1]


def is_palindrome(word: str) -> bool:
    """
    Returns True if word is a palindrome.
    Uses recursion and fruitful function principles.
    """
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


def is_power(a: int, b: int) -> bool:
    """
    Returns True if a is a power of b.
    Base case: a == b
    Recursive case: a is divisible by b AND a/b is a power of b.
    """
    if a == b:
        return True
    if b == 0 or b == 1:
        # Prevent zero division and infinite recursion for b=1
        return False
    if a % b == 0:
        return is_power(a // b, b)
    return False


if __name__ == "__main__":
    print("--- Palindrome Checker ---")
    words = ["noon", "redivider", "python", ""]
    for w in words:
        print(f"'{w}': {is_palindrome(w)}")

    print("\n--- Power Checker ---")
    print(f"Is 8 a power of 2? {is_power(8, 2)}")
    print(f"Is 10 a power of 2? {is_power(10, 2)}")
    print(f"Is 27 a power of 3? {is_power(27, 3)}")
