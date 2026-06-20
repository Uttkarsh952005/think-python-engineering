"""
Chapter 21: Mini Project - Algorithm Profiler
Visually compares the O(n^2) Bubble Sort against Python's highly optimized O(n log n) Timsort.
"""

import random
import time


def bubble_sort(data: list[int]) -> list[int]:
    """O(n^2) time complexity. Simple but incredibly slow for large lists."""
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        # Flag to optimize slightly if already sorted
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def python_sort(data: list[int]) -> list[int]:
    """O(n log n) time complexity. Python uses Timsort internally."""
    return sorted(data)


def profile_sort(sort_func, data: list[int]) -> float:
    """Profiles a single sorting execution."""
    start = time.perf_counter()
    sort_func(data)
    end = time.perf_counter()
    return end - start


def main():
    print("=== Sorting Algorithm Profiler ===")
    print("Comparing O(n^2) Bubble Sort vs O(n log n) Timsort\n")

    # Test on progressively larger datasets
    sizes = [100, 500, 1000, 2000]

    print(f"{'Input Size':<12} | {'Bubble Sort (s)':<18} | {'Timsort (s)':<18}")
    print("-" * 55)

    for size in sizes:
        # Generate random array
        data = [random.randint(0, 10000) for _ in range(size)]

        # Profile both
        bubble_time = profile_sort(bubble_sort, data)
        timsort_time = profile_sort(python_sort, data)

        print(f"{size:<12} | {bubble_time:<18.5f} | {timsort_time:<18.5f}")

    print("\nNotice how Bubble Sort time quadruples when input size doubles (n^2).")


if __name__ == "__main__":
    main()
