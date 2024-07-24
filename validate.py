import json
from collections import Counter

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

# count how many cards of 25 aura points, how many of 25 skill points, and how many of 25 stamina points are in the deck
aura_points_25 = sum(card["aura"] == 25 for card in deck)
skill_points_25 = sum(card["skill"] == 25 for card in deck)
stamina_points_25 = sum(card["stamina"] == 25 for card in deck)

print("\n -- 25 points cards --")
print(f"🧠 Deck has {aura_points_25} cards with 25 aura points")
print(f"🧠 Deck has {skill_points_25} cards with 25 skill points")
print(f"🧠 Deck has {stamina_points_25} cards with 25 stamina points") 

# 24 aura points, 24 skill points, 24 stamina points
aura_points_24 = sum(card["aura"] == 24 for card in deck)
skill_points_24 = sum(card["skill"] == 24 for card in deck)
stamina_points_24 = sum(card["stamina"] == 24 for card in deck)

print("\n -- 24 points cards --")
print(f"🧠 Deck has {aura_points_24} cards with 24 aura points")
print(f"🧠 Deck has {skill_points_24} cards with 24 skill points")
print(f"🧠 Deck has {stamina_points_24} cards with 24 stamina points")

# count occurrences of each score
score_counts = Counter()

for card in deck:
    if "total" in card:
        score_counts[card["total"]] += 1
    else:
        score_counts[card["score"]] += 1

print("\n -- Score counts --")
for score, count in sorted(score_counts.items(), reverse=True):
    print(f"🏆 Score {score}: {count} cards")