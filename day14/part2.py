source_data = 'day14/input.txt'

with open(source_data, 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

starting_point = [x for x in input[0]]
transformations = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in input[2:]}


current_state = {}

# Setup a dict of the current pairs of characters
for x in range(len(starting_point)):
    if not current_state.get(''.join(starting_point[x:x + 2])):
        current_state[''.join(starting_point[x:x + 2])] = 1
    else:
        current_state[''.join(starting_point[x:x + 2])] += 1


def add_item(state, key, value):
    if not state.get(key):
        state[key] = value
    else:
        state[key] += value


for x in range(40):
    next_state = {}
    for key, value in current_state.items():
        if key in transformations:
            add_item(next_state,
                     ''.join([key[0], transformations[key]]),
                     value)
            add_item(next_state,
                     ''.join([transformations[key], key[1]]),
                     value)
        else:
            add_item(next_state, key, value)

    current_state = next_state.copy()

result = {}
for key, value in current_state.items():
    add_item(result, key[0], value)


max_count = max(result, key=result.get)
min_count = min(result, key=result.get)

print(result[max_count] - result[min_count])
