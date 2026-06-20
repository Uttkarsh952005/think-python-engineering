"""
Chapter 9: Mini Project - CLI Shopping Cart
Demonstrates list mutability, passing references, and managing a collection of items.
"""

def display_cart(cart: list[str]) -> None:
    """Displays the current contents of the shopping cart."""
    if not cart:
        print("Your cart is empty.")
        return
        
    print("\n--- Shopping Cart ---")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item}")
    print("---------------------\n")

def add_item(cart: list[str], item: str) -> None:
    """Adds an item to the cart in-place."""
    cart.append(item)
    print(f"Added '{item}' to cart.")

def remove_item(cart: list[str], item: str) -> None:
    """Removes an item from the cart if it exists."""
    if item in cart:
        cart.remove(item)
        print(f"Removed '{item}' from cart.")
    else:
        print(f"Item '{item}' not found in cart.")

def main():
    # The 'state' of our application
    my_cart = []
    
    # Simulating a user session
    display_cart(my_cart)
    
    add_item(my_cart, "Apples")
    add_item(my_cart, "Bread")
    add_item(my_cart, "Milk")
    
    display_cart(my_cart)
    
    # Demonstrate mutability and sorting
    my_cart.sort()
    print("Cart sorted alphabetically.")
    display_cart(my_cart)
    
    remove_item(my_cart, "Bread")
    display_cart(my_cart)

if __name__ == "__main__":
    main()
