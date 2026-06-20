"""
Chapter 8: Mini Project - CLI Text Analyzer
A simple tool that ingests text and provides character-level statistics.
Demonstrates string traversal, counting, and string formatting.
"""


def analyze_text(text: str) -> dict:
    """
    Analyzes the given text and returns a dictionary of stats.
    Focuses on string traversal and character categorization.
    """
    vowels = "aeiouAEIOU"

    stats = {
        "length": len(text),
        "vowels": 0,
        "consonants": 0,
        "spaces": 0,
        "punctuation": 0,
    }

    for char in text:
        if char.isspace():
            stats["spaces"] += 1
        elif char in vowels:
            stats["vowels"] += 1
        elif char.isalpha():  # Since it's not a vowel, it must be a consonant
            stats["consonants"] += 1
        else:
            stats["punctuation"] += 1

    return stats


def display_report(stats: dict) -> None:
    """Formats and prints the analysis report."""
    print("=== Text Analysis Report ===")
    print(f"Total Characters: {stats['length']}")
    print("-" * 28)
    print(f"Vowels:       {stats['vowels']}")
    print(f"Consonants:   {stats['consonants']}")
    print(f"Spaces:       {stats['spaces']}")
    print(f"Punctuation:  {stats['punctuation']}")
    print("============================")


def main():
    sample = (
        "Think Python is a great book! It teaches you how to THINK like a programmer."
    )
    print(f"Analyzing: '{sample}'\n")

    results = analyze_text(sample)
    display_report(results)


if __name__ == "__main__":
    main()
