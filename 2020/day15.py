data = '0,14,1,3,7,9'
# data = '1,3,2'
# data = '2,1,3'
# data = '3,1,2'


def play_game(starting_numbers):
    numbers = {}
    turn = 1
    last_number_spoken = starting_numbers[0]
    # Initialization round
    for number in starting_numbers:
        numbers[number] = [turn]
        last_number_spoken = number
        turn += 1

    # Calculate new number to be spoken
    while True:
        # print(numbers)
        number_to_speak = 0
        if last_number_spoken in numbers and len(numbers[last_number_spoken]) > 1:
            # print('lastnum turn', numbers[last_number_spoken])
            number_to_speak = numbers[last_number_spoken][1] - \
                numbers[last_number_spoken][0]
        # print(last_number_spoken)
        # print('Turn', turn, '->', number_to_speak)
        yield number_to_speak

        if number_to_speak in numbers:
            numbers[number_to_speak].append(turn)
            if len(numbers[number_to_speak]) > 2:
                numbers[number_to_speak].pop(0)
        else:
            numbers[number_to_speak] = [turn]
        last_number_spoken = number_to_speak
        turn += 1


starting_numbers = [int(x) for x in data.split(',')]
game_generator = play_game(starting_numbers)

new_number = 0
# Part 1
number_to_find = 2020 - len(starting_numbers)

# Part 2
number_to_find = 30000000 - len(starting_numbers)
for i in range(number_to_find):
    new_number = next(game_generator)

print(new_number)
