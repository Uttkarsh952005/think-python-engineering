"""
Chapter 16: Mini Project - CLI Card Game (High Card)
Uses the Deck, Card, and Hand classes to orchestrate a simple automated game.
"""
from examples import Deck
from exercises import Hand

def play_high_card(players_names: list[str]) -> None:
    """Plays a simple automated game of High Card."""
    print("=== HIGH CARD ===")
    deck = Deck()
    deck.shuffle()
    
    hands = []
    for name in players_names:
        hands.append(Hand(name))
        
    # Deal one card to each player
    for hand in hands:
        hand.add_card(deck.pop_card())
        
    # Display cards and find winner
    winner = None
    winning_card = None
    
    print("\n--- Dealing ---")
    for hand in hands:
        card = hand.cards[0]
        print(f"{hand.label} draws: {card}")
        
        if winning_card is None or winning_card < card:
            winning_card = card
            winner = hand.label
            
    print("\n--- Result ---")
    print(f"{winner} wins with the {winning_card}!")

def main():
    players = ["Alice", "Bob", "Charlie", "Diana"]
    play_high_card(players)

if __name__ == "__main__":
    main()
