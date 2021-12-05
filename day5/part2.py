import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

source_data = 'day5/input.txt'

with open(source_data, 'r') as f:
    vent_locations = [x.replace('\n', '') for x in f.readlines()]

vent_pairs = [[[int(x) for x in coords.split(',')] for coords in vents_pairs.split(' -> ')] for vents_pairs in vent_locations]
flat_vent_list = [item for sublist in vent_pairs for item in sublist]
flat_vent_x = [x[0] for x in flat_vent_list]
flat_vent_y = [x[1] for x in flat_vent_list]


grid = np.zeros((max(flat_vent_x) + 1, max(flat_vent_y) + 1))

for start, end in vent_pairs:
    if start[0] == end[0]:
        y_coords = [start[1], end[1]]
        y_coords.sort()
        grid[start[0]][y_coords[0]:y_coords[1] + 1] += 1
    elif start[1] == end[1]:
        x_coords = [start[0], end[0]]
        x_coords.sort()
        grid[:, start[1]][x_coords[0]:x_coords[1] + 1] += 1
    else:
        if start[0] < end[0]:
            x_step = 1
            x_start = start[0]
            x_end = end[0] + 1
        else:
            x_step = -1
            x_start = start[0]
            x_end = end[0] - 1
        if start[1] < end[1]:
            y_step = 1
            y_start = start[1]
            y_end = end[1] + 1
        else:
            y_step = -1
            y_start = start[1]
            y_end = end[1] - 1
        for x, y in zip(range(x_start, x_end, x_step), range(y_start, y_end, y_step)):
            grid[x, y] += 1


result = 0
for x in grid:
    for value in x:
        if value > 1:
            result += 1

# Debugging print of the heat map
sns.heatmap(grid.transpose())
plt.savefig('day5/debug2.png', dpi=500)
print(result)


# bigger than 5573
