import numpy as np

source_data = 'day6/input.txt'

with open(source_data, 'r') as f:
    initial_state = [x.replace('\n', '').split(',') for x in f.readlines()]

initial_state = [int(item) for sublist in initial_state for item in sublist]

current_state = {x: 0 for x in range(9)}

for x in initial_state:
    current_state[x] += 1


timestep = range(1, 300)
state = {0: current_state for x in [0]}

for y in timestep:
    state[y] = {}
    for day in range(8):
        state[y][day] = current_state[day + 1]

    state[y][8] = current_state[0]
    state[y][6] += current_state[0]

    current_state = state[y]

# calculate result
result = 0
for x in state[256].values():
    result += x

print(result)
