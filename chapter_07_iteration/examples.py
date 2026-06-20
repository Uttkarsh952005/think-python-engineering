"""
Chapter 7: Iteration
Examples of while loops and iterative state updates.
"""

import math


def countdown(n: int) -> None:
    """Iterative version of countdown."""
    while n > 0:
        print(n)
        n = n - 1
    print("Blastoff!")


def sequence(n: int) -> None:
    """
    Collatz conjecture sequence.
    Demonstrates a loop where the number of iterations is unknown.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = n * 3 + 1
    print(n)


def approximate_sqrt(a: float) -> float:
    """
    Uses Newton's method to approximate a square root.
    Demonstrates iterative approximation until a threshold is met.
    """
    x = a / 2.0  # Initial guess
    epsilon = 1e-15  # Precision threshold

    while True:
        y = (x + a / x) / 2.0
        if abs(y - x) < epsilon:
            break
        x = y
    return x


def main():
    print("--- Collatz Sequence ---")
    sequence(3)

    print("\n--- Newton's Square Root ---")
    val = 25.0
    approx = approximate_sqrt(val)
    print(f"Approx sqrt of {val}: {approx}")
    print(f"Math library sqrt : {math.sqrt(val)}")


if __name__ == "__main__":
    main()
