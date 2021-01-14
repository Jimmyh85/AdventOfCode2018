import math
import aoc_helper
import re
from collections import defaultdict

data = aoc_helper.get_input("input22", "plain").strip()
# data = aoc_helper.get_input("input21_sample", "string")
# print(data)

left, right = data.split("\n\n")
player_A = [int(x) for x in left.split("\n")[1:]]
player_B = [int(x) for x in right.split("\n")[1:]]
# print(player_A)
# print(player_B)

# Game ends if one of the decks is empty
def is_game_over(player_A, player_B):
    if not player_A or not player_B:
        return True
    return False


def calculate_score(player_A, player_B):
    score_A = 0
    score_B = 0
    for i, card in enumerate(reversed(player_A), 1):
        score_A += i * card
    for i, card in enumerate(reversed(player_B), 1):
        score_B += i * card
    return (score_A, score_B)


round = 0

# Part 1
while not is_game_over(player_A, player_B):
    round += 1
    card_A = player_A.pop(0)
    card_B = player_B.pop(0)
    # print(round, card_A, card_B)
    if card_A > card_B:
        player_A += [card_A, card_B]
    elif card_B > card_A:
        player_B += [card_B, card_A]
    else:
        print("equals")

print("Part 1:", calculate_score(player_A, player_B))

# Part 2
def get_deck_snapshot(player_A, player_B):
    return (tuple(player_A), tuple(player_B))


USED = set()


def recursive_combat(player_A, player_B, USED):
    round = 0
    while not is_game_over(player_A, player_B):
        round += 1
        # Check for infinite loops
        deck_snapshot = get_deck_snapshot(player_A, player_B)
        if deck_snapshot in USED:
            return (player_A, [])
        else:
            USED.add(deck_snapshot)

        # Draw cards
        card_A = player_A.pop(0)
        card_B = player_B.pop(0)
        # print(round, card_A, card_B)

        # Check if sub-game must be played
        if card_A <= len(player_A) and card_B <= len(player_B):
            result = recursive_combat(player_A[:card_A], player_B[:card_B], set())
            if result[0] and not result[1]:
                # Player A wins
                player_A += [card_A, card_B]
            elif not result[0] and result[1]:
                # Player B wins
                player_B += [card_B, card_A]
            else:
                print("Error", result)

        # Else, higher card wins
        else:
            if card_A > card_B:
                player_A += [card_A, card_B]
            elif card_B > card_A:
                player_B += [card_B, card_A]
            else:
                print("Error: cards are equal")
    return (player_A, player_B)


# Reset the decks
player_A = [int(x) for x in left.split("\n")[1:]]
player_B = [int(x) for x in right.split("\n")[1:]]

result = recursive_combat(player_A, player_B, set())
print("Part 2:", calculate_score(result[0], result[1]))
