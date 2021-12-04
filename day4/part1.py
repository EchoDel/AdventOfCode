import numpy as np

source_data = 'day4/bingo.txt'

with open(source_data, 'r') as f:
    bingo = [x.replace('\n', '') for x in f.readlines()]

called_number = [int(x) for x in bingo[0].split(',')]
bingo_cards = bingo[2:]

# make the cards

cards = []
card = np.zeros((5, 5))
i = 0
for line in bingo_cards:
    if line == '':
        cards.append(card)
        i = 0
        card = np.zeros((5, 5))
    else:
        card[i] = [int(x) for x in line.replace('  ', ' ').lstrip().split(' ')]
        i += 1


# Setup the winning numbers for each card
winning_numbers = []

for card in cards:
    winnings = []
    winnings.append(card[0])
    winnings.append(card[1])
    winnings.append(card[2])
    winnings.append(card[3])
    winnings.append(card[4])

    winnings.append(card[:, 0])
    winnings.append(card[:, 1])
    winnings.append(card[:, 2])
    winnings.append(card[:, 3])
    winnings.append(card[:, 4])

    winnings.append(np.diagonal(card))
    winnings.append(card[:, ::-1].diagonal())
    winning_numbers.append(winnings)


stop_loop = False

for index in range(len(called_number)):
    for card_index, card_winnings in enumerate(winning_numbers):
        for winnings in card_winnings:
            check = all(item in called_number[:index + 1] for item in winnings)
            if check:
                stop_loop = True
                break
        if stop_loop:
            break
    if stop_loop:
        break

# Found the right card, and the number it occured, and all check number. Just got to find the score
latest_number = called_number[:index + 1][-1]
card_numbers = cards[card_index].flatten().tolist()
sum_of_unmarked_numbers = 0

for number in card_numbers:
    if int(number) in called_number[:index + 1]:
        print(number)
    else:
        sum_of_unmarked_numbers += number

print(sum_of_unmarked_numbers * latest_number)


