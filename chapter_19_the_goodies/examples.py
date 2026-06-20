"""
Chapter 19: The Goodies
Examples of list comprehensions, generators, and the collections module.
"""

from collections import Counter, defaultdict


def demonstrate_comprehensions() -> None:
    """Shows the evolution from loops to comprehensions."""
    numbers = [1, 2, 3, 4, 5]

    # 1. The old way
    squares_loop = []
    for n in numbers:
        squares_loop.append(n**2)

    # 2. The Pythonic way (List Comprehension)
    squares_comp = [n**2 for n in numbers]

    # 3. With filtering
    even_squares = [n**2 for n in numbers if n % 2 == 0]

    print(f"Squares (Comp): {squares_comp}")
    print(f"Even Squares:   {even_squares}")


def demonstrate_generators() -> None:
    """Shows lazy evaluation using generator expressions."""
    # Note the parentheses instead of square brackets
    gen = (x**2 for x in range(3))

    print("\nGenerator output:")
    print(next(gen))  # 0
    print(next(gen))  # 1
    print(next(gen))  # 4


def demonstrate_collections() -> None:
    """Shows how collections simplify counting and grouping."""
    text = "to be or not to be that is the question"
    words = text.split()

    # Using Counter
    word_counts = Counter(words)
    print(f"\nCounter: {word_counts}")
    print(f"Most common: {word_counts.most_common(2)}")

    # Using defaultdict for grouping by first letter
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)

    print(f"DefaultDict Grouping: {dict(grouped)}")


def main():
    print("--- The Goodies ---")
    demonstrate_comprehensions()
    demonstrate_generators()
    demonstrate_collections()

    print("\n--- Any and All ---")
    bools = [True, True, False]
    print(f"any(bools): {any(bools)}")  # True if at least one is True
    print(f"all(bools): {all(bools)}")  # True only if ALL are True


if __name__ == "__main__":
    main()
