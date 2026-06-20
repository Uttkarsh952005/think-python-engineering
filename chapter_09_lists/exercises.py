"""
Chapter 9: Exercises
Applying map, filter, and reduce patterns to lists.
"""

def nested_sum(t: list[list[int]]) -> int:
    """
    Takes a list of lists of integers and adds up the elements from all the nested lists.
    (A 'reduce' operation).
    """
    total = 0
    for nested_list in t:
        total += sum(nested_list)
    return total

def cumulative_sum(t: list[int]) -> list[int]:
    """
    Takes a list of numbers and returns the cumulative sum.
    (A 'map' operation with running state).
    """
    result = []
    current_sum = 0
    for num in t:
        current_sum += num
        result.append(current_sum)
    return result

def is_sorted(t: list) -> bool:
    """
    Takes a list as a parameter and returns True if the list is sorted
    in ascending order and False otherwise.
    """
    # Compare original list with a sorted copy
    # Note: Timsort (Python's sorting algorithm) is highly optimized for already sorted lists.
    return t == sorted(t)

if __name__ == "__main__":
    print("--- Nested Sum ---")
    t = [[1, 2], [3], [4, 5, 6]]
    print(f"{t} -> {nested_sum(t)}")
    
    print("\n--- Cumulative Sum ---")
    t2 = [1, 2, 3]
    print(f"{t2} -> {cumulative_sum(t2)}")
    
    print("\n--- Is Sorted ---")
    print(f"[1, 2, 2]: {is_sorted([1, 2, 2])}")
    print(f"['b', 'a']: {is_sorted(['b', 'a'])}")
