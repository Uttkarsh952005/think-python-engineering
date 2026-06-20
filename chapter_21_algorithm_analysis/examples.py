"""
Chapter 21: Analysis of Algorithms
Examples comparing the time complexity of different data structures.
"""

import timeit


def find_in_list(data: list, target: int) -> bool:
    """O(n) Linear Time lookup."""
    return target in data


def find_in_set(data: set, target: int) -> bool:
    """O(1) Constant Time lookup."""
    return target in data


def main():
    print("--- Big O Notation: List vs Set Lookup ---")

    # Create a large dataset
    size = 10_000_000
    print(f"Generating dataset of {size} integers...")
    large_list = list(range(size))
    large_set = set(large_list)

    # Target is at the very end of the collection (worst case scenario)
    target = size - 1

    print("\nMeasuring List Lookup (O(n)):")
    # timeit runs the code multiple times to get an accurate measurement
    list_time = timeit.timeit(lambda: find_in_list(large_list, target), number=10)
    print(f"Time: {list_time:.5f} seconds")

    print("\nMeasuring Set Lookup (O(1)):")
    set_time = timeit.timeit(lambda: find_in_set(large_set, target), number=10)
    print(f"Time: {set_time:.5f} seconds")

    if set_time > 0:
        speedup = list_time / set_time
        print(
            f"\nThe O(1) Set was approximately {speedup:.0f}x faster for this dataset."
        )


if __name__ == "__main__":
    main()
