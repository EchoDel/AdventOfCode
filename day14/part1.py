source_data = 'day14/input.txt'

with open(source_data, 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

starting_point = [x for x in input[0]]
transformations = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in input[2:]}


current_state = starting_point.copy()

for step in range(10):
    next_state = []
    for x in range(len(current_state)):
        if ''.join(current_state[x:x+2]) in transformations.keys():
            next_state.append(current_state[x])
            next_state.append(transformations[''.join(current_state[x:x+2])])
        else:
            next_state.append(current_state[x])

    current_state = next_state.copy()

count = {x: 0 for x in set(current_state)}

for value in current_state:
    count[value] += 1

max_count = max(count, key=count.get)
min_count = min(count, key=count.get)

print(count[max_count] - count[min_count])
