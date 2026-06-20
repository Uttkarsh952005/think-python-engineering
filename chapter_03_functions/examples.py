"""
Chapter 3: Functions
Examples exploring function definitions, arguments, and local scope.
"""

def print_lyrics() -> None:
    """Prints classic Monty Python lyrics. Demonstrates a basic function without parameters."""
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics() -> None:
    """Demonstrates function composition by calling another function."""
    print_lyrics()
    print_lyrics()

def print_twice(bruce: str) -> None:
    """Demonstrates a function with a parameter."""
    print(bruce)
    print(bruce)

def main():
    # Calling functions
    print("--- Lyrics ---")
    repeat_lyrics()
    
    print("\n--- Print Twice ---")
    # Passing arguments
    print_twice("Spam")
    
    # Passing expressions as arguments
    print_twice("Spam " * 4)

if __name__ == "__main__":
    main()
