"""
Chapter 20: Mini Project - Execution Tracer
A custom decorator that logs the inputs and outputs of any function to help trace bugs.
"""

import functools
import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def trace(func):
    """
    A decorator that logs the entry, arguments, and exit of a function.
    Highly useful for tracing recursive functions or complex pipelines.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join([repr(a) for a in args])
        kwarg_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [arg_str, kwarg_str]))

        logging.debug(f"[ENTER] {func.__name__}({all_args})")

        # Execute the actual function
        try:
            result = func(*args, **kwargs)
            logging.debug(f"[EXIT]  {func.__name__} returned {repr(result)}")
            return result
        except Exception as e:
            logging.error(f"[ERROR] {func.__name__} raised {type(e).__name__}: {e}")
            raise

    return wrapper


@trace
def factorial(n: int) -> int:
    """Recursive function to demonstrate the tracer."""
    if n < 0:
        raise ValueError("Cannot compute factorial of negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    print("--- Decorator Execution Tracer ---")
    print("\nTracing successful execution:")
    factorial(3)

    print("\nTracing an error state:")
    try:
        factorial(-1)
    except ValueError:
        pass  # Expected


if __name__ == "__main__":
    main()
