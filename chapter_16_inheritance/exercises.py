"""
Chapter 16: Exercises
Implementing a Hand class that inherits from Deck.
"""

# Importing Deck and Card from our examples file to maintain DRY principles
from examples import Deck, Card

class Hand(Deck):
    """
    Represents a hand of playing cards.
    Demonstrates Inheritance (IS-A Deck).
    """
    
    def __init__(self, label: str = ''):
        """
        Overrides Deck.__init__. A hand starts empty, 
        unlike a deck which starts with 52 cards.
        """
        self.cards = []
        self.label = label

    def move_cards(self, hand: 'Hand', num: int) -> None:
        """Moves a given number of cards from this hand to another."""
        for _ in range(num):
            if self.cards:
                hand.add_card(self.pop_card())

if __name__ == "__main__":
    print("--- Inheritance Demo ---")
    deck = Deck()
    deck.shuffle()
    
    # Hand inherits add_card, pop_card, and __str__ from Deck
    hand = Hand("Player 1")
    
    print(f"{hand.label} starts with {len(hand.cards)} cards.")
    
    # Deal 5 cards
    deck.move_cards(hand, 5) # Wait, deck doesn't have move_cards!
    # Let's manually pop for the demo, since we only added move_cards to Hand
    for _ in range(5):
         hand.add_card(deck.pop_card())
         
    print(f"{hand.label} now has {len(hand.cards)} cards:")
    print(hand)
    
    # Test move_cards between hands
    hand2 = Hand("Player 2")
    hand.move_cards(hand2, 2)
    print(f"\nMoved 2 cards from {hand.label} to {hand2.label}")
    print(f"{hand2.label}'s cards:")
    print(hand2)
