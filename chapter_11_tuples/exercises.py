"""
Chapter 11: Exercises
Practicing *args, tuple swapping, and the DSU pattern.
"""


def sumall(*args: float) -> float:
    """
    Takes any number of arguments and returns their sum.
    Uses Python's built-in sum() on the gathered tuple.
    """
    return sum(args)


def sort_by_length(words: list[str]) -> list[str]:
    """
    Sorts a list of words from longest to shortest using DSU.
    (Decorate, Sort, Undecorate)
    """
    # 1. Decorate: Build a list of tuples (length, random_tiebreaker, word)
    # Note: Modern Python sorts stably, but we'll use standard DSU logic.
    decorated = []
    for word in words:
        decorated.append((len(word), word))

    # 2. Sort: Python sorts tuples by comparing the first element.
    # If there's a tie, it compares the second element.
    decorated.sort(reverse=True)

    # 3. Undecorate: Extract just the words
    result = []
    for length, word in decorated:
        result.append(word)

    return result


if __name__ == "__main__":
    print("--- sumall ---")
    print(f"sumall(1, 2, 3) = {sumall(1, 2, 3)}")
    print(f"sumall(10.5, 20.2) = {sumall(10.5, 20.2)}")

    print("\n--- Sort by Length (DSU) ---")
    animals = ["macaque", "baboon", "chimpanzee", "ape", "gorilla"]
    sorted_animals = sort_by_length(animals)
    print(f"Original: {animals}")
    print(f"Sorted:   {sorted_animals}")
