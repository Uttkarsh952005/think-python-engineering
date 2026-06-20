"""
Chapter 10: Exercises
Using dictionaries to optimize algorithms.
"""

def has_duplicates(t: list) -> bool:
    """
    Checks if a list has any duplicate elements.
    By using a dictionary, we reduce the time complexity from O(n^2) to O(n).
    """
    seen = {}
    for item in t:
        if item in seen:
            return True
        seen[item] = True
    return False

def build_word_dict(word_list: list[str]) -> dict:
    """
    Stores a list of words as keys in a dictionary for O(1) lookups.
    The values don't matter, we just use empty strings.
    """
    word_dict = {}
    for word in word_list:
        word_dict[word] = ""
    return word_dict

if __name__ == "__main__":
    print("--- Has Duplicates (Optimized) ---")
    test_list_1 = [1, 2, 3, 4, 5]
    test_list_2 = [1, 2, 3, 2, 5]
    
    print(f"{test_list_1} -> {has_duplicates(test_list_1)}")
    print(f"{test_list_2} -> {has_duplicates(test_list_2)}")
    
    print("\n--- Dictionary Lookup Speed ---")
    # Simulating a large dictionary
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    fast_lookup = build_word_dict(words)
    
    print(f"Is 'cherry' in dict? {'cherry' in fast_lookup}") # O(1) time
    print(f"Is 'fig' in dict? {'fig' in fast_lookup}")
