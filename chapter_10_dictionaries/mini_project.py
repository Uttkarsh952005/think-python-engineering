"""
Chapter 10: Mini Project - CLI Word Frequency Analyzer
Analyzes a block of text, strips punctuation, and outputs the top N most frequent words.
Demonstrates dictionaries as counters and sorting dictionary data.
"""


def clean_word(word: str) -> str:
    """Strips punctuation and converts to lowercase."""
    cleaned = ""
    for char in word:
        if char.isalpha():
            cleaned += char.lower()
    return cleaned


def analyze_frequencies(text: str) -> dict[str, int]:
    """Builds a frequency dictionary from a raw string of text."""
    words = text.split()
    freq = {}

    for word in words:
        cw = clean_word(word)
        if cw:  # ignore empty strings from purely punctuation 'words'
            freq[cw] = freq.get(cw, 0) + 1

    return freq


def print_top_words(freq: dict[str, int], limit: int = 5) -> None:
    """
    Sorts the dictionary by frequency and prints the top results.
    """
    # Create a list of tuples (frequency, word) to allow sorting by frequency
    freq_list = []
    for word, count in freq.items():
        freq_list.append((count, word))

    # Sort in descending order
    freq_list.sort(reverse=True)

    print(f"--- Top {limit} Most Frequent Words ---")
    for count, word in freq_list[:limit]:
        print(f"{word}: {count}")


def main():
    sample_text = """
    Python is an interpreted, high-level and general-purpose programming language. 
    Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
    Its language constructs and object-oriented approach aim to help programmers write clear, 
    logical code for small and large-scale projects. Python is dynamically typed and garbage-collected.
    """

    frequencies = analyze_frequencies(sample_text)
    print_top_words(frequencies, limit=5)


if __name__ == "__main__":
    main()
