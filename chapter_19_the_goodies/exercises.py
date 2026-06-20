"""
Chapter 19: Exercises
Refactoring old problems using modern Pythonic features.
"""


def has_duplicates_old(lst: list) -> bool:
    """The procedural way to check for duplicates."""
    seen = []
    for item in lst:
        if item in seen:
            return True
        seen.append(item)
    return False


def has_duplicates_pythonic(lst: list) -> bool:
    """
    The Pythonic way.
    A set automatically removes duplicates. If the length changed,
    duplicates existed.
    """
    return len(lst) != len(set(lst))


def get_word_lengths(words: list[str]) -> dict[int, list[str]]:
    """
    Groups words by their length.
    Uses dictionary comprehensions and advanced sorting.
    """
    # Dictionary comprehension mapping length to a list of words of that length
    return {
        length: [w for w in words if len(w) == length]
        for length in set(len(w) for w in words)
    }


if __name__ == "__main__":
    print("--- Has Duplicates ---")
    data1 = [1, 2, 3, 4, 5]
    data2 = [1, 2, 3, 2, 5]

    print(f"Data 1 duplicates? {has_duplicates_pythonic(data1)}")
    print(f"Data 2 duplicates? {has_duplicates_pythonic(data2)}")

    print("\n--- Dictionary Comprehensions ---")
    words = ["apple", "bat", "car", "banana", "dog", "elephant"]
    grouped = get_word_lengths(words)

    for length, w_list in sorted(grouped.items()):
        print(f"{length} letters: {w_list}")
