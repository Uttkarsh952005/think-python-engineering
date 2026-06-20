"""
Chapter 20: Debugging
Examples of using assertions and logging to catch state mutations early.
"""

import logging

# Configure basic logging instead of using print()
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def calculate_average(numbers: list[float]) -> float:
    """Calculates the average of a list, demonstrating defensive programming."""

    # Defensive Assertion: Fail fast if input is invalid
    assert isinstance(numbers, list), "Input must be a list"

    if not numbers:
        logging.warning("Empty list provided to calculate_average. Returning 0.")
        return 0.0

    logging.debug(f"Calculating average for {len(numbers)} items.")
    total = sum(numbers)

    # Semantic check: Total shouldn't magically be negative if inputs are positive
    if all(n >= 0 for n in numbers):
        assert total >= 0, "Total of positive numbers must be positive"

    return total / len(numbers)


def main():
    print("--- Defensive Programming & Logging ---")

    # Valid case
    avg1 = calculate_average([10, 20, 30])
    print(f"Average 1: {avg1}")

    # Edge case caught by logging
    avg2 = calculate_average([])
    print(f"Average 2: {avg2}")

    # Type error caught by assertion
    try:
        calculate_average("1, 2, 3")  # Not a list
    except AssertionError as e:
        print(f"Assertion caught bug before it propagated: {e}")


if __name__ == "__main__":
    main()
