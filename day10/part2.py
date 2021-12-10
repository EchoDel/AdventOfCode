from math import floor

import numpy as np

source_data = 'day10/input.txt'

with open(source_data, 'r') as f:
    navigation = [x.replace('\n', '') for x in f.readlines()]

pairs = {'(': ')',
         '[': ']',
         '{': '}',
         '<': '>'}

points = {')': 1,
          ']': 2,
          '}': 3,
          '>': 4}

incomplete = []
result = 0

for original_line in navigation:
    line = original_line
    for x in range(10):
        line = line.replace('[]', '')
        line = line.replace('()', '')
        line = line.replace('{}', '')
        line = line.replace('<>', '')

    if len([x for x in pairs.values() if x in line]) == 0:
        incomplete.append(line)


scores = []
for subline in incomplete:
    correction = []
    score = 0
    for x in subline[::-1]:
        correction.append(pairs[x])
        score = score * 5 + points[pairs[x]]
    scores.append(score)

scores.sort()
print(scores[floor(len(scores) / 2)])


# < 2275343571