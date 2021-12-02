import pandas as pd

source_data = 'day1/depths.txt'

with open(source_data, 'r') as f:
    depths = f.readlines()

depths = [int(depth.replace('\n', '')) for depth in depths]


depths = pd.DataFrame(depths)
depths.columns = ['depth']
depths['rollsum'] = depths['depth'].rolling(window=3).sum()

increasing = 0
for current_depth, next_depth in zip(depths['rollsum'][0:-1], depths['rollsum'][1:]):
    if current_depth < next_depth:
        increasing += 1
