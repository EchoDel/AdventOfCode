import numpy as np

source_data = 'day10/input.txt'

with open(source_data, 'r') as f:
    navigation = [x.replace('\n', '') for x in f.readlines()]

score = {')': 3,
         ']': 57,
         '}': 1197,
         '>': 25137}

incomplete = []
result = 0

for original_line in navigation:
    line = original_line
    for x in range(10):
        line = line.replace('[]', '')
        line = line.replace('()', '')
        line = line.replace('{}', '')
        line = line.replace('<>', '')

    if len([x for x in score.keys() if x in line]) == 0:
        incomplete.append(original_line)
    else:
        for character in line:
            if character in score.keys():
                result += score[character]
                break

print(result)
