"""
Chapter 1: The Way of the Program
Examples focusing on basic output, syntax, and understanding the interpreter.
"""


def main():
    # The foundational building block of interaction
    print("Hello, World!")

    # Exploring basic arithmetic and the strictness of formal languages
    # If we miss a parenthesis, the interpreter will complain—this is expected and helpful.
    minutes = 45
    hours = minutes / 60
    print(f"{minutes} minutes is {hours} hours.")


if __name__ == "__main__":
    main()
