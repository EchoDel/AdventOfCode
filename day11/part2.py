import numpy as np

source_data = 'day11/input2.txt'

with open(source_data, 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

grid = np.zeros((len(input[0]), len(input)))

# Setup the grid
for x, x_row in enumerate(input):
    for y, value in enumerate(x_row):
        grid[x, y] = input[x][y]


def natural_increase(grid):
    # do step
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            grid[x, y] += 1
    return grid


def do_flashes(grid):
    visited = []
    last_step = 0
    flow_flashes = True

    while flow_flashes:
        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                if grid[x, y] > 9:
                    to_update_x = [0]
                    to_update_y = [0]
                    if (x, y) not in visited:
                        visited.append((x, y))
                    else:
                        continue
                    # get a list of octopus to uppate
                    if x > 0:
                        to_update_x.append(-1)
                    if x < grid.shape[0] - 1:
                        to_update_x.append(1)
                    if y > 0:
                        to_update_y.append(-1)
                    if y < grid.shape[1] - 1:
                        to_update_y.append(1)

                    for move_x in to_update_x:
                        for move_y in to_update_y:
                            grid[x + move_x, y + move_y] += 1

        if len(visited) == last_step:
            flow_flashes = False
        else:
            last_step = len(visited)

        for x, y in visited:
            grid[x, y] = 0

    return grid, len(visited)


next_grid = grid.copy()
steps = 0
while True:

    natural_grid = natural_increase(next_grid).copy()
    flashed_grid, flashes = do_flashes(natural_grid)

    if flashes == 100:
        break
    steps += 1
    next_grid = flashed_grid.copy()

print(steps + 1)
