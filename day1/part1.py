source_data = 'day1/depths.txt'

with open(source_data, 'r') as f:
    depths = f.readlines()

depths = [int(depth.replace('\n', '')) for depth in depths]

increasing = 0
for current_depth, next_depth in zip(depths[0:-1], depths[1:]):
    if current_depth < next_depth:
        increasing += 1
