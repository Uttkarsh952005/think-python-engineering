"""
Chapter 6: Fruitful Functions
Examples of functions that compute and return values.
"""
import math

def absolute_value(x: float) -> float:
    """Returns the absolute value of x."""
    if x < 0:
        return -x
    return x

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculates the Euclidean distance between two points."""
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    return math.sqrt(dsquared)

def circle_area(xc: float, yc: float, xp: float, yp: float) -> float:
    """
    Calculates the area of a circle given its center (xc, yc) 
    and a point on the perimeter (xp, yp).
    Demonstrates function composition.
    """
    radius = distance(xc, yc, xp, yp)
    return math.pi * radius**2

def is_divisible(x: int, y: int) -> bool:
    """
    A boolean function. Returns True if x is strictly divisible by y.
    """
    return x % y == 0

def main():
    print("--- Absolute Value ---")
    print(f"Abs of -5: {absolute_value(-5)}")
    
    print("\n--- Circle Area via Composition ---")
    # Center at (0,0), perimeter point at (3,4)
    # Radius will be 5, Area will be pi * 25
    area = circle_area(0, 0, 3, 4)
    print(f"Area: {area:.2f}")

    print("\n--- Boolean Functions ---")
    print(f"Is 6 divisible by 3? {is_divisible(6, 3)}")
    print(f"Is 7 divisible by 3? {is_divisible(7, 3)}")

if __name__ == "__main__":
    main()
