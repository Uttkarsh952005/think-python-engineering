"""
Chapter 19: Mini Project - Advanced Text Analyzer
Utilizes the collections module and generators to process text efficiently.
"""

import re
from collections import Counter


def clean_text(text: str) -> list[str]:
    """Uses regex and list comprehensions to sanitize input."""
    # Convert to lowercase and find all alphanumeric words
    words = re.findall(r"\b[a-z]+\b", text.lower())
    return words


def analyze_document(text: str) -> None:
    """Provides advanced statistics using Pythonic idioms."""
    words = clean_text(text)

    if not words:
        print("No words found.")
        return

    print("=== Text Analysis Report ===")

    # 1. Total Words
    print(f"Total Words: {len(words)}")

    # 2. Unique Words (using sets)
    unique_words = set(words)
    print(f"Unique Words: {len(unique_words)}")

    # 3. Lexical Richness (Unique / Total)
    richness = len(unique_words) / len(words)
    print(f"Lexical Richness: {richness:.2%}")

    # 4. Longest word using max with a key function
    longest = max(unique_words, key=len)
    print(f"Longest Word: '{longest}' ({len(longest)} chars)")

    # 5. Most common words using Counter
    word_freq = Counter(words)
    print("\nTop 5 Most Frequent Words:")
    for word, count in word_freq.most_common(5):
        print(f"  - {word}: {count}")


def main():
    sample_text = """
    Python is an interpreted, high-level and general-purpose programming language. 
    Python's design philosophy emphasizes code readability with its notable use 
    of significant indentation. Its language constructs and object-oriented 
    approach aim to help programmers write clear, logical code for small and 
    large-scale projects.
    """
    analyze_document(sample_text)


if __name__ == "__main__":
    main()
