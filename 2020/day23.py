# data = "389125467"
data = "198753462"

cups = [int(item) for item in list(data)]
# Part 2
for i in range(len(data) + 1, 1_000_001):
    cups.append(i)
print(len(cups))
# For Part 2 we need a data structure with fast access to an item of the list an its successors
successors = {}
for k, v in zip(cups, cups[1:]):
    successors[k] = v
successors[cups[-1]] = cups[0]
# print(data)
# print(successors)

# print(cups)
MIN_CUP = min(cups)
MAX_CUP = max(cups)
MOVE_LIMIT = 10_000_000
move = 1

current_cup = cups[0]
destination_cup = None

while move <= MOVE_LIMIT:
    # print("\n-- move", move, " --")

    # 1. Pick up three cups right to the current_cup
    circle_length = len(cups)
    cup_1 = successors[current_cup]
    cup_2 = successors[cup_1]
    cup_3 = successors[cup_2]
    next_current_cup = successors[cup_3]
    # print("cups: ", cups)
    # print("Current cup: ", current_cup)
    # print("picked up: ", cup_1, cup_2, cup_3)
    # 2. Find destination cup
    destination_cup = current_cup - 1
    while (
        destination_cup in [cup_1, cup_2, cup_3]
        or not MIN_CUP <= destination_cup <= MAX_CUP
    ):
        if destination_cup < MIN_CUP:
            destination_cup = MAX_CUP
        else:
            destination_cup = destination_cup - 1
    # print("destination:", destination_cup)

    # 3. Append picked up cups
    successors[cup_3] = successors[destination_cup]
    successors[destination_cup] = cup_1
    successors[current_cup] = next_current_cup

    # 4. Select new current cup
    current_cup = next_current_cup
    move += 1

# print(successors)
# idx = 1
# ans = ""
# while successors[idx] != 1:
#     ans += str(successors[idx])
#     idx = successors[idx]
# print("Part 1:", ans)
print("Part 2:", successors[1] * successors[successors[1]])
