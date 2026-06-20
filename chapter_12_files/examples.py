"""
Chapter 12: Files
Examples of file I/O, context managers, and exception handling.
"""
import os

def write_sample_file(filename: str) -> None:
    """Writes lines to a file safely using a context manager."""
    # 'w' mode overwrites. 'a' would append.
    with open(filename, 'w') as f:
        f.write("Line 1: Hello File System\n")
        f.write("Line 2: Data Persistence\n")
        f.write("Line 3: Goodbye\n")
    print(f"Wrote to {filename}")

def read_file_safely(filename: str) -> None:
    """Demonstrates reading and exception handling."""
    try:
        with open(filename, 'r') as f:
            print(f"--- Reading {filename} ---")
            for line in f:
                # strip() removes the trailing newline character
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Do not have permission to read '{filename}'.")

def main():
    test_file = "test_output.txt"
    
    # 1. Handle a missing file gracefully
    read_file_safely("does_not_exist.txt")
    print()
    
    # 2. Write and Read
    write_sample_file(test_file)
    read_file_safely(test_file)
    
    # Clean up (optional, good practice for temporary examples)
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\nCleaned up {test_file}")

if __name__ == "__main__":
    main()
