"""
Chapter 8: Exercises
String manipulation, reverse traversal, and boolean functions.
"""

def print_backward(s: str) -> None:
    """Prints a string backward, one character per line."""
    index = len(s) - 1
    while index >= 0:
        print(s[index])
        index -= 1

def is_reverse(word1: str, word2: str) -> bool:
    """
    Returns True if word1 is the reverse of word2.
    Demonstrates index alignment between two sequences.
    """
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1
    
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
        
    return True

def rotate_word(word: str, shift: int) -> str:
    """
    Implements a basic Caesar cipher character rotation.
    Shifts each letter by the given amount.
    """
    rotated = ""
    for char in word:
        if char.isalpha():
            # Determine base based on casing
            base = ord('a') if char.islower() else ord('A')
            # Shift character, wrap around alphabet, and append
            new_ord = (ord(char) - base + shift) % 26 + base
            rotated += chr(new_ord)
        else:
            # Leave punctuation/spaces untouched
            rotated += char
    return rotated

if __name__ == "__main__":
    print("--- Backward Traversal ---")
    print_backward("pot")
    
    print("\n--- Reverse Checker ---")
    print(f"pots / stop: {is_reverse('pots', 'stop')}")
    print(f"pots / step: {is_reverse('pots', 'step')}")
    
    print("\n--- Word Rotator (Caesar Cipher) ---")
    print(f"cheer rotated by 7: {rotate_word('cheer', 7)}")
    print(f"melon rotated by -10: {rotate_word('melon', -10)}")
