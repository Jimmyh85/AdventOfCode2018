import aoc_helper

data = aoc_helper.get_input("4", "plain")
data_split = data.split("\n\n")

numbers = [int(num) for num in data_split[0].split(",")]
# print(numbers)

# Skipt first and last entry to get our raw bingo board data
boards = [[[int(col) for col in row.split()] for row in board] for board in [line.split("\n") for line in data_split[1:-1]]]
# print(boards)

# for board in boards:
#     print(board)
#     for row in board:
#         print(row.split())
# print(boards)

ROWS = len(boards[0])
COLS = len(boards[0][0])

# print(ROWS, COLS)

def is_winner(board, numbers):
    # Check all in a row
    for c in range(COLS):
        row_count = 0
        for r in range(ROWS):
            if board[c][r] not in numbers:
                break
            else:
                row_count += 1
                if row_count == ROWS:
                    return True

    # Check all in column
    for c in range(COLS):
        col_count = 0
        for r in range(ROWS):
            if board[r][c] not in numbers:
                break
            else:
                col_count += 1
                if col_count == COLS:
                    return True

    return False

i = 5
# print(len(numbers))

#numbers = [34, 90, 18, 33, 83]
winning_boards = []
while i <= len(numbers) and len(boards) > 0:
    current_numbers = numbers[0:i]
    # print(current_numbers)
    for board in boards:
        if is_winner(board, current_numbers):
            # print("Winner", board, i, current_numbers)
            # # Calculate score
            # all_board_numbers = aoc_helper.flatten_list(board)
            # score = sum([num for num in all_board_numbers if num not in current_numbers]) * current_numbers[-1]
            winning_boards.append((board, i))
            # remove board from board list
            boards.remove(board)
            
    i = i + 1

# Part 1
first_winning_board, first_number = winning_boards[0]
current_numbers = numbers[0:first_number]
score = sum([num for num in aoc_helper.flatten_list(first_winning_board) if num not in current_numbers]) * current_numbers[-1]
print("Part 1", score)

# Part 2
last_winning_board, last_number = winning_boards[-1]
current_numbers = numbers[0:last_number]
score = sum([num for num in aoc_helper.flatten_list(last_winning_board) if num not in current_numbers]) * current_numbers[-1]
print("Part 2", score)
