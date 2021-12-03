import pandas as pd

source_data = 'day3/diagnostic_report.txt'

with open(source_data, 'r') as f:
    report = f.readlines()

report = {int(line.replace('\n', ''), 2): line.replace('\n', '') for line in report}

data = report.copy()

for bit in range(11, -1, -1):
    result = {0: 0, 1: 0}
    for line in data:
        result[line >> bit & 1] += 1

    if result[0] == result[1]:
        maximum = 1
    else:
        maximum = max(result, key=result.get)

    data = {key: value for key, value in data.items() if value[11-bit] == str(maximum)}

    if len(data) == 1:
        oxygen = list(data.keys())[0]


data = report.copy()

for bit in range(11, -1, -1):
    result = {0: 0, 1: 0}
    for line in data:
        result[line >> bit & 1] += 1

    if result[0] == result[1]:
        minimum = 0
    else:
        minimum = min(result, key=result.get)
    data = {key: value for key, value in data.items() if value[11-bit] == str(minimum)}

    if len(data) == 1:
        co2 = list(data.keys())[0]
        break

lifesupport = co2 * oxygen

print(lifesupport)
