"""
Chapter 10: Dictionaries
Examples of mapping, the histogram pattern, and handling missing keys.
"""

def histogram(s: str) -> dict[str, int]:
    """
    Creates a histogram (frequency counter) of characters in a string.
    Demonstrates the standard dictionary accumulation pattern.
    """
    d = dict()
    for char in s:
        # If char isn't in d, get() returns 0. Then we add 1.
        d[char] = d.get(char, 0) + 1
    return d

def print_hist(h: dict) -> None:
    """Iterates over a dictionary and prints keys and values."""
    for key, val in h.items():
        print(f"{key}: {val}")

def reverse_lookup(d: dict, v: any) -> list:
    """
    Finds all keys that map to a specific value.
    This is an O(n) operation (slow compared to a forward lookup).
    """
    keys = []
    for key, val in d.items():
        if val == v:
            keys.append(key)
    return keys

def main():
    word = "brontosaurus"
    print(f"--- Histogram of '{word}' ---")
    hist = histogram(word)
    print_hist(hist)
    
    print("\n--- Reverse Lookup ---")
    target_freq = 2
    keys_with_freq = reverse_lookup(hist, target_freq)
    print(f"Characters appearing exactly {target_freq} times: {keys_with_freq}")

if __name__ == "__main__":
    main()
