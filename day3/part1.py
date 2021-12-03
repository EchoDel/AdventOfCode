import pandas as pd

source_data = 'day3/diagnostic_report.txt'

with open(source_data, 'r') as f:
    report = f.readlines()

report = [int(line.replace('\n', ''), 2) for line in report]

result = {x: {0: 0, 1: 0, } for x in range(12)}

for line in report:
    for bit in range(12):
        result[bit][line >> bit & 1] += 1

gamma = []
epsilon = []

for bit in result.values():
    gamma.append(str(max(bit, key=bit.get)))
    epsilon.append(str(min(bit, key=bit.get)))

gamma.reverse()
epsilon.reverse()

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

power = gamma * epsilon
print(power)
