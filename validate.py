import json

# deck file path
deck_file_path = "deck.json"

# read the deck from the file
with open(deck_file_path, "r") as deck_file:
    deck = json.load(deck_file)

# validate the deck by checking if there are only 20 cards in the deck
if len(deck) == 20:
    print("Deck contains 20 cards")
else:
    print("Deck is invalid. It should contain 20 cards")

# validate the deck by checking that each card is unique
deck_as_frozensets = {frozenset(card.items()) for card in deck}
if len(deck) == len(deck_as_frozensets):
    print("All cards are unique")
else:
    print("Deck is invalid. All cards should be unique")