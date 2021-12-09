import numpy as np

source_data = 'day9/input.txt'

with open(source_data, 'r') as f:
    heights = [x.replace('\n', '') for x in f.readlines()]

height_map = np.zeros((len(heights), len(heights[0]),))

for x, x_row in enumerate(height_map):
    for y, value in enumerate(x_row):
        height_map[x, y] = heights[x][y]

results = {}
for x, x_row in enumerate(height_map):
    for y, value in enumerate(x_row):
        surroundings = []
        if x > 0:
            surroundings.append(height_map[x - 1, y])
        if x < height_map.shape[0] -1:
            surroundings.append(height_map[x+1, y])
        if y > 0:
            surroundings.append(height_map[x, y-1])
        if y < height_map.shape[1] - 1:
            surroundings.append(height_map[x, y+1])
        if value < min(surroundings):
            results[x, y] = value

print(sum([x+1 for x in results.values()]))
