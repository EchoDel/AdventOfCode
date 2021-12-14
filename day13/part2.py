from math import floor

import numpy as np
import seaborn as sns

source_data = 'day13/input.txt'

with open(source_data, 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

starting_points = []
folds = []
for line in input:
    if line == '':
        continue
    elif line[0] == 'f':
        folds.append((line.split('=')[0].split(' ')[-1], int(line.split('=')[1])))
    else:
        starting_points.append([int(point) for point in line.split(',')])

max_x = max([x for x, y in starting_points])
max_y = max([y for x, y in starting_points])

grid = np.zeros((max_y + 1, max_x + 1,))

for x, y in starting_points:
    grid[y, x] = 1

for direction, line in folds:
    if direction == 'x':
        new_grid = np.zeros((grid.shape[0], floor(grid.shape[1] / 2)))
        for y, x_row in enumerate(grid):
            for x, value in enumerate(x_row):
                if x == line:
                    continue
                if x > line:
                    new_grid[y, grid.shape[1] - x - 1] = max(value, new_grid[y, grid.shape[1] - x - 1])
                else:
                    new_grid[y, x] = value

    if direction == 'y':
        new_grid = np.zeros((floor(grid.shape[0] / 2), grid.shape[1]))
        for y, x_row in enumerate(grid):
            for x, value in enumerate(x_row):
                if y == line:
                    continue
                if y > line:
                    new_grid[grid.shape[0] - y - 1, x] = max(value, new_grid[grid.shape[0] - y - 1, x])
                else:
                    new_grid[y, x] = value
    grid = new_grid


ax = sns.heatmap(grid)
