import pandas as pd

source_data = 'day2/course.txt'

with open(source_data, 'r') as f:
    course = f.readlines()

course = [depth.replace('\n', '') for depth in course]


depth = 0
distance = 0

for action in course:
    action, value = action.split(' ')
    if action == 'forward':
        distance += int(value)
    if action == 'up':
        depth -= int(value)
    if action == 'down':
        depth += int(value)

depth * distance
