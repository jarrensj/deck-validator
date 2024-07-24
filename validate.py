import json

# deck file path
deck_file_path = "deck.json"

# read the deck from the file
with open(deck_file_path, "r") as deck_file:
    deck = json.load(deck_file)

# validate the deck by checking if there are only 20 cards in the deck
if len(deck) == 20:
    print("✅ Deck contains 20 cards")
else:
    print("❌ Deck is invalid. It should contain 20 cards")

# validate the deck by checking that each card is unique
deck_as_frozensets = {frozenset(card.items()) for card in deck}
if len(deck) == len(deck_as_frozensets):
    print("✅ All cards are unique")
else:
    print("❌ Deck is invalid. All cards should be unique")

# count how many rarity points are in the deck and validate that the total rarity points are 15 or less
rarity_points = sum(card["rarity"] for card in deck)
if rarity_points <= 15:
    print(f"✅ Deck has {rarity_points} rarity points")
else:
    print(f"❌ Deck is invalid. It has {rarity_points} rarity points, but should have 15 or less")