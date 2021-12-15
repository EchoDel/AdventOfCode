import heapq
import itertools as it
import math

import numpy as np
from typing import Dict, Iterable, Tuple
import networkx as nx

source_data = 'day15/input.txt'
times_bigger = 5

with open(source_data, 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

grid = np.zeros((len(input[0]), len(input)))

# Setup the grid
for x, x_row in enumerate(input):
    for y, value in enumerate(x_row):
        grid[x, y] = input[x][y]


def grid_adjs(
    coord: Tuple[int, ...],
    bounds: Tuple[Tuple[int, int], ...] = None) -> Iterable[Tuple[int, ...]]:
    """
    Compute the compass adjacencies for a given :math:`n`-dimensional point. Bounds can
    be specified, and only adjacent coordinates within those bounds will be returned.
    Bounds can be specified as any one of the :class:`BoundsType`s.
    :param coord: coordinate to calculate the adjacencies of
    :param bounds: ``(high, low)`` tuples for each of the dimensions
    :param adjs_type: the :class:`AdjacenciesType` to use
    :param bounds_type: the :class:`BoundsType` to use
    """
    # Iterate through all of the deltas for the N dimensions of the coord. A delta is
    # -1, 0, or 1 indicating that the adjacent cell is one lower, same level, or higher
    # than the given coordinate.
    for delta in it.product((-1, 0, 1), repeat=len(coord)):
        if all(d == 0 for d in delta):
            # This is the coord itself, skip.
            continue

        if sum(map(abs, delta)) > 1:
            # For compass adjacencies, we only care when there's only one dimension
            # different than the coordinate.
            continue

        if bounds is not None:
            in_bounds = True
            for i, (d, (low, high)) in enumerate(zip(delta, bounds)):
                in_bounds &= low <= coord[i] + d < high
                if not in_bounds:
                    continue

            if not in_bounds:
                continue
        yield tuple(c + d for c, d in zip(coord, delta))


graph = nx.DiGraph()
for r, line in enumerate(input):
    for c, char in enumerate(line):
        graph.add_node((r, c))


for r, line in enumerate(input):
    for c, char in enumerate(line):
        for r1, c1 in grid_adjs((r, c), ((0, len(input)), (0, len(input[0])))):
            graph.add_edge((r, c), (r1, c1), weight=grid[r1, c1])

print(nx.shortest_path(graph, (0, 0), (99, 99), 'weight'))
print(nx.shortest_path_length(graph, (0, 0), (99, 99), 'weight'))

# part 1 = 392
# part 2 = 2823
