"""
Chapter 12: Exercises
Writing a basic search-and-replace utility.
"""


def sed(pattern: str, replacement: str, src: str, dest: str) -> None:
    """
    Reads a source file and writes to a destination file,
    replacing all occurrences of a pattern string with a replacement string.
    Catches errors if files cannot be opened.
    """
    try:
        with open(src, "r") as f_in, open(dest, "w") as f_out:
            for line in f_in:
                # Replace occurrences in the current line
                new_line = line.replace(pattern, replacement)
                f_out.write(new_line)
        print(f"Successfully processed {src} -> {dest}")

    except FileNotFoundError:
        print(f"Error: Source file '{src}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Create a dummy file for the exercise
    dummy_src = "dummy_src.txt"
    dummy_dest = "dummy_dest.txt"

    with open(dummy_src, "w") as f:
        f.write("I love cats.\nCats are great.\nMy cat is asleep.\n")

    print("--- Running SED Exercise ---")
    # Replace "cat" with "dog"
    sed("cat", "dog", dummy_src, dummy_dest)

    print("\n--- Verifying Output ---")
    with open(dummy_dest, "r") as f:
        print(f.read().strip())

    # Clean up
    import os

    os.remove(dummy_src)
    os.remove(dummy_dest)
