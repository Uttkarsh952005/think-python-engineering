"""
Chapter 11: Tuples
Examples of tuple assignment, variable arguments, and zip.
"""

def split_email(email: str) -> tuple[str, str]:
    """Returns the username and domain of an email address."""
    parts = email.split('@')
    # Returns a tuple (username, domain)
    return parts[0], parts[1]

def print_all(*args) -> None:
    """
    Takes an arbitrary number of arguments and packs them into a tuple.
    """
    print(f"Packed args tuple: {args}")

def demonstrate_zip() -> None:
    """Shows how to interleave sequences."""
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    
    # zip pairs up elements. We cast to list to see the result.
    zipped = list(zip(names, scores))
    print(f"Zipped: {zipped}")
    
    # Very useful for creating dictionaries
    score_dict = dict(zip(names, scores))
    print(f"As Dictionary: {score_dict}")

def main():
    print("--- Tuple Assignment & Return Values ---")
    user, domain = split_email("engineer@example.com")
    print(f"User: {user}, Domain: {domain}")
    
    print("\n--- Variable Arguments ---")
    print_all(1, 2.0, "Three")
    
    print("\n--- Zip ---")
    demonstrate_zip()

if __name__ == "__main__":
    main()
