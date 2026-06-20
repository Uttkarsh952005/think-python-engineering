"""
Chapter 5: Exercises
Applying conditional logic and recursion.
"""

def check_fermat(a: int, b: int, c: int, n: int) -> None:
    """
    Checks if Fermat's Last Theorem holds.
    Fermat says a^n + b^n = c^n is impossible for n > 2.
    """
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def is_triangle(a: int, b: int, c: int) -> None:
    """
    Determines if three side lengths can form a triangle.
    If any of the three lengths is greater than the sum of the other two, 
    then you cannot form a triangle.
    """
    # Using early returns (guard clauses) for clean logic
    if a > b + c or b > a + c or c > a + b:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    print("--- Fermat's Theorem Checker ---")
    check_fermat(3, 4, 5, 2) # Should not work since n is not > 2
    check_fermat(3, 4, 5, 3) 
    
    print("\n--- Triangle Checker ---")
    is_triangle(1, 2, 3) # Degenerate triangle, usually "Yes" depending on strictness
    is_triangle(1, 2, 4) # Cannot form
