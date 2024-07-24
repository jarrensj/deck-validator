import json
from collections import Counter, defaultdict

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

# count and store card names for 25 points and 24 points cards
aura_25_cards = [card["name"] for card in deck if card["aura"] == 25]
skill_25_cards = [card["name"] for card in deck if card["skill"] == 25]
stamina_25_cards = [card["name"] for card in deck if card["stamina"] == 25]

aura_24_cards = [card["name"] for card in deck if card["aura"] == 24]
skill_24_cards = [card["name"] for card in deck if card["skill"] == 24]
stamina_24_cards = [card["name"] for card in deck if card["stamina"] == 24]

print("\n -- 25 points cards --")
print(f"\n🧠 Deck has {len(aura_25_cards)} cards with 25 aura points:")
for name in aura_25_cards:
    print(f"  - {name}")
print(f"\n🧠 Deck has {len(skill_25_cards)} cards with 25 skill points:")
for name in skill_25_cards:
    print(f"  - {name}")
print(f"\n🧠 Deck has {len(stamina_25_cards)} cards with 25 stamina points:")
for name in stamina_25_cards:
    print(f"  - {name}")

print("\n -- 24 points cards --")
print(f"\n🧠 Deck has {len(aura_24_cards)} cards with 24 aura points:")
for name in aura_24_cards:
    print(f"  - {name}")
print(f"\n🧠 Deck has {len(skill_24_cards)} cards with 24 skill points:")
for name in skill_24_cards:
    print(f"  - {name}")
print(f"\n🧠 Deck has {len(stamina_24_cards)} cards with 24 stamina points:")
for name in stamina_24_cards:
    print(f"  - {name}")

# count occurrences of each score and store card names
score_counts = Counter()
score_card_names = defaultdict(list)

for card in deck:
    if "total" in card:
        score = card["total"]
    else:
        score = card["score"]
    score_counts[score] += 1
    score_card_names[score].append(card["name"])

print("\n -- Score counts --")
for score, count in sorted(score_counts.items(), reverse=True):
    print(f"\n🏆 Score {score}: {count} cards")
    for name in score_card_names[score]:
        print(f"  - {name}")
