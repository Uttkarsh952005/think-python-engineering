"""
Chapter 3: Mini Project - CLI Receipt Generator
A simple application to demonstrate function composition, string formatting, 
and building cohesive logic from small, focused functions.
"""

def format_header(store_name: str) -> str:
    """Returns a formatted receipt header."""
    return f"=== {store_name.upper()} ===\n"

def format_item(item_name: str, price: float) -> str:
    """Formats a single item and its price aligned to the right."""
    # Format price to 2 decimal places
    price_str = f"${price:.2f}"
    # Calculate spacing to keep lines 30 characters wide
    spacing = 30 - len(item_name) - len(price_str)
    return f"{item_name}{' ' * max(1, spacing)}{price_str}"

def format_total(total: float) -> str:
    """Formats the total price section."""
    divider = "-" * 30
    total_str = f"TOTAL: ${total:.2f}"
    return f"{divider}\n{total_str.rjust(30)}"

def generate_receipt(store_name: str, items: list[tuple[str, float]]) -> None:
    """
    Main function composing the receipt from smaller formatting functions.
    """
    print(format_header(store_name))
    
    total = 0.0
    for name, price in items:
        print(format_item(name, price))
        total += price
        
    print(format_total(total))

if __name__ == "__main__":
    purchases = [
        ("Apples", 2.50),
        ("Bread", 3.00),
        ("Peanut Butter", 4.99),
        ("Coffee", 12.50)
    ]
    generate_receipt("Python Grocers", purchases)
