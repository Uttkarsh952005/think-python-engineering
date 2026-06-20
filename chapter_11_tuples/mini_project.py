"""
Chapter 11: Mini Project - Anagram Grouper
Finds all anagrams in a list of words.
Demonstrates using a tuple as a dictionary key because it is hashable.
"""

def signature(word: str) -> tuple[str, ...]:
    """
    Returns a sorted tuple of letters in the word.
    Anagrams will have the exact same signature.
    """
    # sorted() returns a list. We must convert to tuple to use as a dict key.
    return tuple(sorted(word.lower()))

def group_anagrams(words: list[str]) -> dict[tuple, list[str]]:
    """
    Groups words by their anagram signature.
    """
    anagram_dict = {}
    
    for word in words:
        sig = signature(word)
        if sig not in anagram_dict:
            anagram_dict[sig] = []
        anagram_dict[sig].append(word)
        
    return anagram_dict

def main():
    word_list = [
        "deltas", "desalt", "lasted", "salted", "slated", "staled",
        "retain", "retina", "tear", "rate", "tare"
    ]
    
    grouped = group_anagrams(word_list)
    
    print("--- Anagram Groups ---")
    for sig, words in grouped.items():
        if len(words) > 1:
            print(f"Signature {''.join(sig)}: {words}")

if __name__ == "__main__":
    main()
