source_data = 'day17/input.txt'

with open(source_data, 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

target = [[int(y) for y in x.split('=')[1].split('..')] for x in input[0].split(',')]

x = target[0]
y = target[1]
options = {}

testing_velocities = range(200)
for x_test in testing_velocities:
    for y_test in testing_velocities:
        current_velocity = [x_test, y_test]
        current_location = [0, 0]
        max_y = 0
        while current_location[1] >= y[0]:
            current_location = list(map(sum, zip(current_velocity, current_location)))
            current_velocity[0] = max(0, current_velocity[0] - 1)
            current_velocity[1] = current_velocity[1] - 1
            max_y = max(max_y, current_location[1])
            if (current_location[0] <= x[1]) and \
                (current_location[0] >= x[0]) and \
                (current_location[1] <= y[1]) and \
                (current_location[1] >= y[0]):
                options[(x_test, y_test)] = max_y
                break


print(max(options.values()))


# > 2926