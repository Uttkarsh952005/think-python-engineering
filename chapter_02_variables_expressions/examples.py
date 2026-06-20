"""
Chapter 2: Variables, Expressions, and Statements
Examples exploring state, data types, and operations.
"""

def calculate_sphere_volume(radius: float) -> float:
    """Calculates the volume of a sphere given its radius."""
    # Using variables to clarify the mathematical formula
    pi = 3.14159
    volume = (4 / 3) * pi * (radius ** 3)
    return volume

def main():
    # Demonstrating meaningful variable names
    message = "And now for something completely different"
    n = 17
    pi_approximation = 3.14159

    print(f"Message: {message}")
    print(f"Integer: {n}")
    print(f"Float: {pi_approximation}")

    # Example calculation
    r = 5
    vol = calculate_sphere_volume(r)
    print(f"Volume of a sphere with radius {r} is {vol:.2f}")

if __name__ == "__main__":
    main()
