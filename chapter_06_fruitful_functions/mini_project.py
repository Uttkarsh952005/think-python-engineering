"""
Chapter 6: Mini Project - Functional CLI Calculator
Demonstrates pure fruitful functions and basic command parsing.
Avoids global state, using return values to pass data.
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def evaluate_expression(op: str, a: float, b: float) -> float:
    """
    Maps an operator string to the corresponding mathematical function.
    """
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        raise ValueError(f"Unknown operator: {op}")


def main():
    print("--- Functional CLI Calculator ---")
    # In a real app, this would come from user input using input()
    # For demonstration, we'll process a batch of expressions.
    expressions = [("+", 10, 5), ("-", 20, 7), ("*", 3, 4.5), ("/", 100, 4)]

    for op, a, b in expressions:
        try:
            result = evaluate_expression(op, a, b)
            print(f"{a} {op} {b} = {result}")
        except ValueError as e:
            print(f"Error evaluating {a} {op} {b}: {e}")


if __name__ == "__main__":
    main()
