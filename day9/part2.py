import numpy as np
from skimage.morphology import flood_fill

source_data = 'day9/input.txt'

with open(source_data, 'r') as f:
    heights = [x.replace('\n', '') for x in f.readlines()]

height_map = np.zeros((len(heights), len(heights[0]),))

# change the height map to 1 and 0 since those are the only values we care about
for x, x_row in enumerate(height_map):
    for y, value in enumerate(x_row):
        if heights[x][y] == '9':
            height_map[x, y] = 1
        else:
            height_map[x, y] = 0


# Flood fill the grid starting from a zero point with the next numbers
current_flood_value = 2
updated_height_map = height_map
for x in range(updated_height_map.shape[0]):
    for y in range(updated_height_map.shape[1]):
        if updated_height_map[x, y] == 0:
            updated_height_map = flood_fill(updated_height_map, (x, y), current_flood_value, connectivity=1)
            current_flood_value += 1


sizes = {x: 0 for x in range(current_flood_value)}

for x, x_row in enumerate(updated_height_map):
    for y, value in enumerate(x_row):
        sizes[value] += 1

# Set 1 to zero to make sure that the max is actually the valleys
sizes[1] = 0

maximum = sorted(sizes, key=sizes.get, reverse=True)


result = 1
for x in maximum[:3]:
    result *= sizes[x]

print(result)
