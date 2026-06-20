"""
Chapter 4: Case Study - Interface Design
Examples demonstrating encapsulation and generalization using the turtle module.
Note: Running this will open a graphical window.
"""

import turtle


def draw_square(t: turtle.Turtle, length: int) -> None:
    """
    Draws a square with the given turtle and side length.
    Demonstrates encapsulation (wrapping logic in a function)
    and generalization (using a length parameter).
    """
    for _ in range(4):
        t.fd(length)
        t.lt(90)


def main():
    # Setup the environment
    bob = turtle.Turtle()

    # Use our encapsulated function
    draw_square(bob, 100)

    # Wait for user to close window
    turtle.mainloop()


if __name__ == "__main__":
    # In an automated testing environment, we might skip the GUI.
    # We will run main() directly for the educational example.
    # main()
    print("Run this script directly to see the turtle draw a square.")
