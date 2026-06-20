"""
Chapter 7: Exercises
Practicing iterative algorithms and loop control.
"""
import math

def test_square_root() -> None:
    """
    Prints a table comparing our custom iterative square root
    against the built-in math.sqrt().
    """
    # Inline definition from examples to keep exercise self-contained
    def mysqrt(a: float) -> float:
        x = a / 2.0
        while True:
            y = (x + a / x) / 2.0
            if abs(y - x) < 1e-15:
                break
            x = y
        return x

    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    
    for a in range(1, 10):
        a_float = float(a)
        my_val = mysqrt(a_float)
        math_val = math.sqrt(a_float)
        diff = abs(my_val - math_val)
        
        # Format the table for neat columns
        print(f"{a_float:<3} {my_val:<13.11f} {math_val:<13.11f} {diff}")

def eval_loop() -> None:
    """
    Iteratively evaluates user input until the user types 'done'.
    Demonstrates the `while True` and `break` pattern.
    """
    print("Welcome to eval_loop. Type valid python expressions or 'done' to exit.")
    last_result = None
    
    while True:
        user_input = input(">>> ")
        if user_input.strip() == 'done':
            break
        try:
            # Note: eval() is unsafe in production, but used here 
            # strictly for the Think Python exercise context.
            last_result = eval(user_input)
            print(last_result)
        except Exception as e:
            print(f"Error: {e}")
            
    print(f"Loop finished. Last successful result: {last_result}")

if __name__ == "__main__":
    print("--- Square Root Table ---")
    test_square_root()
    
    print("\n--- Eval Loop (Uncomment to test) ---")
    # eval_loop()
