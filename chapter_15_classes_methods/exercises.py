"""
Chapter 15: Exercises
Implementing a Point class with magic methods.
"""


class Point:
    """Represents a point in 2D space."""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other) -> "Point":
        """
        Adds two points, or a point and a tuple.
        Demonstrates type-based dispatch.
        """
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Point(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("Unsupported operand type for +")


if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(10, 20)

    print("--- Point String Representation ---")
    print(f"p1: {p1}")
    print(f"p2: {p2}")

    print("\n--- Point Addition ---")
    p3 = p1 + p2
    print(f"p1 + p2: {p3}")

    print("\n--- Type Dispatch Addition ---")
    p4 = p1 + (5, 5)
    print(f"p1 + (5, 5): {p4}")
