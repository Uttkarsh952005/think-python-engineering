"""
Chapter 21: Exercises
Implementing and comparing search algorithms.
"""

import timeit


def linear_search(data: list[int], target: int) -> int:
    """
    O(n) time. Scans every element from start to finish.
    Returns the index, or -1 if not found.
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data: list[int], target: int) -> int:
    """
    O(log n) time. Requires a SORTED list.
    Cuts the search space in half each iteration.
    Returns the index, or -1 if not found.
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = data[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def main():
    print("--- Search Algorithms ---")
    size = 1_000_000
    # Must be sorted for binary search to work!
    data = list(range(size))
    target = size - 1  # Worst case for linear

    print(f"Searching for {target} in a list of {size} items...")

    print("\nLinear Search (O(n)):")
    lin_time = timeit.timeit(lambda: linear_search(data, target), number=10)
    print(f"Time: {lin_time:.5f}s")

    print("\nBinary Search (O(log n)):")
    bin_time = timeit.timeit(lambda: binary_search(data, target), number=10)
    print(f"Time: {bin_time:.5f}s")


if __name__ == "__main__":
    main()
