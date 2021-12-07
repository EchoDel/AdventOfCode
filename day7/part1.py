from matplotlib import pyplot as plt

source_data = 'day7/input.txt'

with open(source_data, 'r') as f:
    initial_state = [x.replace('\n', '').split(',') for x in f.readlines()]

initial_list = [int(item) for sublist in initial_state for item in sublist]


initial_state = {x:0 for x in range(max(initial_list) + 1)}

for value in initial_list:
    initial_state[value] += 1


costs = {}
for final_location in range(max(initial_list) + 1):
    cost = 0
    for key, value in initial_state.items():
        cost += abs(key - final_location) * value

    costs[final_location] = cost
#
# plt.plot([x for x in costs.values()])
# plt.savefig('day7/debug_debug.png', dpi=500)

print(min(costs.values()))