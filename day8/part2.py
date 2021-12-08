source_data = 'day8/input.txt'

with open(source_data, 'r') as f:
    display = [x.replace('\n', '') for x in f.readlines()]

results = [x.split('| ')[1].split(' ') for x in display]

result = 0
for number in display:
    code, coded_result = number.split(' | ')

    # Decode the screen
    sorted_code = [sorted(x) for x in sorted(code.split(' '), key=len)]
    split_coded_result = [''.join(sorted(x)) for x in coded_result.split(' ')]

    # Try to find the coded digits
    known_coded_characters = {x: 0 for x in range(10)}
    # 1 is the only digit with 2 lines
    known_coded_characters[1] = sorted_code[0]
    # 7 is the only digit with 3 lines
    known_coded_characters[7] = sorted_code[1]
    # 4 is the only digit with 4 lines
    known_coded_characters[4] = sorted_code[2]
    # 8 is the only digit with 7 lines
    known_coded_characters[8] = sorted_code[-1]
    # 6 is the only character with 6 lines and none from the 1
    known_coded_characters[6] = [x for x in sorted_code
                                 if (len(x) == 6) and
                                 (sum([char in known_coded_characters[1] for char in x]) == 1)][0]

    # 9 has 6 characters and includes all from 4
    known_coded_characters[9] = [x for x in sorted_code
                                 if (len(x) == 6) and
                                 (sum([char in known_coded_characters[4] for char in x]) == 4)][0]

    # 0 is the only missing 6 character digit
    known_coded_characters[0] = [x for x in sorted_code
                                 if (len(x) == 6) and
                                 x != known_coded_characters[6] and
                                 x != known_coded_characters[9]][0]

    # 5 has all lines from 6 intersect 9
    characters_5 = [value for value in known_coded_characters[6] if value in known_coded_characters[9]]
    known_coded_characters[5] = [x for x in sorted_code if x == characters_5][0]

    # 3 includes all lines from the 7
    known_coded_characters[3] = [x for x in sorted_code
                                 if (len(x) == 5) and
                                 (sum([char in known_coded_characters[7] for char in x]) == 3)][0]

    # 2 is the only missing 6 character digit
    known_coded_characters[2] = [x for x in sorted_code
                                 if (len(x) == 5) and
                                 x != known_coded_characters[5] and
                                 x != known_coded_characters[3]][0]

    decode_dict = {''.join(value): key for key, value in known_coded_characters.items()}

    single_result = int(''.join([str(decode_dict[x]) for x in split_coded_result]))
    result += single_result

print(result)
