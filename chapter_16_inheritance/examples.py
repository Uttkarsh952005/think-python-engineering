"""
Chapter 16: Inheritance
Demonstrating class attributes, inheritance, and composition using standard playing cards.
"""
import random

class Card:
    """Represents a standard playing card."""
    
    # Class Attributes (Shared among all instances)
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit: int = 0, rank: int = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        # Accessing class attributes
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

    def __lt__(self, other: 'Card') -> bool:
        """Overloads the < operator for sorting."""
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    """Represents a deck of cards. Demonstrates Composition (HAS-A Card)."""
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self) -> str:
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self) -> Card:
        return self.cards.pop()

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

def main():
    print("--- Card Object ---")
    card1 = Card(2, 11) # Jack of Hearts
    print(card1)
    
    print("\n--- Deck Object ---")
    deck = Deck()
    print(f"Deck created with {len(deck.cards)} cards.")
    deck.shuffle()
    
    print("Drawing top 3 cards:")
    for _ in range(3):
        print(f"  - {deck.pop_card()}")

if __name__ == "__main__":
    main()
