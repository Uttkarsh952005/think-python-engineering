"""
Chapter 4: Mini Project - Generative Art Configurator
Uses the principles of interface design to draw multiple shapes based on a config.
"""

import turtle


def draw_shape(t: turtle.Turtle, shape_type: str, size: int, color: str) -> None:
    """
    Interface for drawing varying shapes.
    Hides the implementation details of the turtle module.
    """
    t.color(color)
    t.begin_fill()

    if shape_type == "square":
        for _ in range(4):
            t.fd(size)
            t.lt(90)
    elif shape_type == "triangle":
        for _ in range(3):
            t.fd(size)
            t.lt(120)

    t.end_fill()


def render_scene(shapes_config: list[dict]) -> None:
    """
    Reads a list of configurations and delegates to draw_shape.
    Demonstrates clean separation of data (config) and logic.
    """
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    for config in shapes_config:
        # Move to position
        t.penup()
        t.goto(config.get("x", 0), config.get("y", 0))
        t.pendown()

        # Draw
        draw_shape(
            t,
            config.get("type", "square"),
            config.get("size", 50),
            config.get("color", "white"),
        )


if __name__ == "__main__":
    # Data-driven design
    scene = [
        {"type": "square", "size": 100, "color": "red", "x": -50, "y": -50},
        {"type": "triangle", "size": 80, "color": "blue", "x": 100, "y": 50},
        {"type": "square", "size": 40, "color": "yellow", "x": -150, "y": 100},
    ]

    print("Uncomment below lines to run the generative scene.")
    # render_scene(scene)
    # turtle.mainloop()
