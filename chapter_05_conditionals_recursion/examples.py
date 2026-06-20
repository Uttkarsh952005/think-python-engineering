"""
Chapter 5: Conditionals and Recursion
Examples demonstrating logical flow and the mechanics of recursion.
"""


def print_parity(x: int) -> None:
    """Demonstrates alternative execution."""
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")


def countdown(n: int) -> None:
    """
    Demonstrates basic recursion.
    Base case: n <= 0
    Recursive step: n > 0, calls countdown(n-1)
    """
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


def main():
    print("--- Conditionals ---")
    print_parity(17)
    print_parity(42)

    print("\n--- Recursion ---")
    countdown(3)


if __name__ == "__main__":
    main()
