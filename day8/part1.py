import numpy as np

source_data = 'day8/input.txt'

with open(source_data, 'r') as f:
    display = [x.replace('\n', '') for x in f.readlines()]

results = [x.split('| ')[1].split(' ') for x in display]

result_characters = [item for sublist in results for item in sublist]

print(len([x for x in result_characters if len(x) in [2, 3, 4, 7]]))
