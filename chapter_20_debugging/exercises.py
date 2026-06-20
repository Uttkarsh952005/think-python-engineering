"""
Chapter 20: Exercises
Debugging a faulty function using a test suite.
"""


def buggy_reverse_list(lst: list) -> list:
    """
    INTENTIONAL BUG: Attempts to reverse a list but modifies the original
    in place in a destructive way while returning None.
    """
    lst.reverse()
    # Semantic bug: reverse() returns None, so this returns None.
    # It also mutated the input, which a pure function shouldn't do.


def fixed_reverse_list(lst: list) -> list:
    """The corrected pure function."""
    # Slicing creates a new reversed copy, leaving the original intact
    return lst[::-1]


def run_tests():
    print("--- Running Test Suite ---")
    original = [1, 2, 3]

    # Test 1: Does it return a list?
    result = fixed_reverse_list(original)
    assert isinstance(result, list), "Should return a list"

    # Test 2: Is it actually reversed?
    assert result == [3, 2, 1], f"Expected [3, 2, 1], got {result}"

    # Test 3: Did it mutate the original input? (Purity check)
    assert original == [1, 2, 3], "Original list was mutated!"

    print("All tests passed! The function is semantically sound.")


if __name__ == "__main__":
    run_tests()
