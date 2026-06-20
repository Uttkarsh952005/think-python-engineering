"""
Chapter 4: Exercises
Refactoring shape drawing functions.
"""

import math
import turtle


def polygon(t: turtle.Turtle, n: int, length: float) -> None:
    """
    Draws an n-sided regular polygon.

    Precondition: n >= 3, length > 0
    """
    angle = 360.0 / n
    for _ in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t: turtle.Turtle, r: float) -> None:
    """
    Draws a circle with the given radius.
    Refactored to use the polygon function (approximation).
    """
    circumference = 2 * math.pi * r
    n = 50  # approximation steps
    length = circumference / n
    polygon(t, n, length)


def arc(t: turtle.Turtle, r: float, angle: float) -> None:
    """
    Draws an arc with the given radius and angle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for _ in range(n):
        t.fd(step_length)
        t.lt(step_angle)


if __name__ == "__main__":
    print(
        "Shape drawing functions defined. Use a python interpreter to test with turtle."
    )
