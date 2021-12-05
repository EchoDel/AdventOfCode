import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

source_data = 'day5/debug.txt'

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


result = 0
for x in grid:
    for value in x:
        if value > 1:
            result += 1

# Debugging print of the heat map
sns.heatmap(grid.transpose())
plt.savefig('day5/debug1.png', dpi=500)
print(result)


# bigger than 5573
