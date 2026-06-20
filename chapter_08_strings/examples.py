"""
Chapter 8: Strings
Examples demonstrating string traversal, slicing, and immutability concepts.
"""


def traverse_string(s: str) -> None:
    """Idiomatic string traversal."""
    for char in s:
        print(char, end="-")
    print()


def find_character(word: str, target: str, start: int = 0) -> int:
    """
    Searches for a character in a string starting at a given index.
    Returns the index if found, -1 otherwise.
    """
    index = start
    while index < len(word):
        if word[index] == target:
            return index
        index += 1
    return -1


def count_a(word: str) -> int:
    """Counts occurrences of 'a' using traversal."""
    count = 0
    for letter in word:
        if letter == "a":
            count = count + 1
    return count


def main():
    fruit = "banana"

    print("--- Traversal ---")
    traverse_string(fruit)

    print("\n--- Slicing ---")
    print(f"fruit[:3]  = {fruit[:3]}")
    print(f"fruit[3:]  = {fruit[3:]}")
    print(f"fruit[::-1] = {fruit[::-1]} (reversed)")

    print("\n--- Searching ---")
    print(f"Index of 'n' starting at 0: {find_character(fruit, 'n', 0)}")
    print(f"Index of 'n' starting at 3: {find_character(fruit, 'n', 3)}")

    print("\n--- Counting ---")
    print(f"Count of 'a' in banana: {count_a(fruit)}")


if __name__ == "__main__":
    main()
