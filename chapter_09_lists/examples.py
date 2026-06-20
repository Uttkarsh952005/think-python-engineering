"""
Chapter 9: Lists
Examples demonstrating mutability, aliasing, and list methods.
"""


def demonstrate_mutability() -> None:
    """Shows how list elements can be reassigned."""
    cheeses = ["Cheddar", "Edam", "Gouda"]
    print(f"Original: {cheeses}")
    cheeses[0] = "Brie"
    print(f"Modified: {cheeses}")


def demonstrate_aliasing() -> None:
    """Highlights the difference between copies and aliases."""
    a = [1, 2, 3]
    b = a  # b is an alias for a
    c = a[:]  # c is a full copy of a

    a[0] = 99
    print(f"a: {a}")
    print(f"b (alias): {b}  <- Notice this changed!")
    print(f"c (copy):  {c}  <- This remained independent.")


def delete_head(t: list) -> None:
    """
    Modifies a list in-place. Because lists are passed by reference,
    changes here affect the caller's list.
    """
    if len(t) > 0:
        del t[0]


def main():
    print("--- Mutability ---")
    demonstrate_mutability()

    print("\n--- Aliasing ---")
    demonstrate_aliasing()

    print("\n--- In-place Modification ---")
    letters = ["a", "b", "c"]
    print(f"Before delete_head: {letters}")
    delete_head(letters)
    print(f"After delete_head: {letters}")


if __name__ == "__main__":
    main()
