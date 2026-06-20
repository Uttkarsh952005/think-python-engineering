"""
Chapter 5: Mini Project - Recursive Tower of Hanoi
A classic computer science problem solved elegantly with recursion.
It highlights how recursion simplifies complex sequential logic.
"""

def solve_hanoi(n: int, source: str, target: str, auxiliary: str) -> None:
    """
    Recursively solves the Tower of Hanoi puzzle.
    
    :param n: Number of disks
    :param source: Name of the source peg
    :param target: Name of the target peg
    :param auxiliary: Name of the auxiliary peg
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Step 1: Move n-1 disks from source to auxiliary, using target as temporary
    solve_hanoi(n - 1, source, auxiliary, target)
    
    # Step 2: Move the nth (largest) disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Step 3: Move the n-1 disks from auxiliary to target, using source as temporary
    solve_hanoi(n - 1, auxiliary, target, source)

def main():
    disks = 3
    print(f"Solving Tower of Hanoi for {disks} disks:\n")
    solve_hanoi(disks, source='A', target='C', auxiliary='B')

if __name__ == "__main__":
    main()
