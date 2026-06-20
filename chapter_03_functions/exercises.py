"""
Chapter 3: Exercises
Practical implementations of function concepts.
"""


def right_justify(s: str) -> None:
    """
    Prints the given string with enough leading spaces so that the
    last letter of the string is in column 70 of the display.
    """
    spaces_needed = 70 - len(s)
    # Ensure we don't multiply by a negative number if string is > 70
    spaces = " " * max(0, spaces_needed)
    print(spaces + s)


def draw_grid() -> None:
    """
    Draws a 2x2 grid using basic print statements.
    Demonstrates abstracting repetitive structural code.
    """

    def draw_row_boundary():
        print("+ - - - - + - - - - +")

    def draw_row_body():
        print("|         |         |")
        print("|         |         |")
        print("|         |         |")
        print("|         |         |")

    draw_row_boundary()
    draw_row_body()
    draw_row_boundary()
    draw_row_body()
    draw_row_boundary()


if __name__ == "__main__":
    print("--- Right Justify ---")
    right_justify("monty")
    right_justify("python")

    print("\n--- Draw Grid ---")
    draw_grid()
