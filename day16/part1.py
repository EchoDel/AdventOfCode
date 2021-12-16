source_data = 'day16/input.txt'

with open(source_data, 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

# Convert to int so we can do bit operations
input_string = bin(int(input[0], 16)).replace('0b', '').zfill(len(input[0]) * 4)


versions = []
def parse_packet(current_string, sum_of_versions=versions):
    print(current_string)
    # print(current_string)
    packet_version = int(current_string[:3], 2)
    sum_of_versions.append(packet_version)
    packet_type = int(current_string[3:6], 2)
    if packet_type == 4:
        leading_bit = '1'
        start = 6
        result = ''
        while leading_bit == '1':
            leading_bit = current_string[start]
            content = current_string[(start + 1): (start + 5)]
            result = result + content
            start += 5
        value = int(result, 2)
        # processed_length = round(start / 4) * 4
        processed_length = start
        return {'packet_version': packet_version,
                'packet_type': packet_type,
                'value': value,
                'processed_length': processed_length}
    else:
        packet_length = int(current_string[6], 2)
        value = {}
        if packet_length == 0:
            expected_length = int(current_string[7:(7 + 15)], 2)
            parsed_length = 0
            expected_results = expected_length
            while parsed_length < expected_length:
                result = parse_packet(current_string[(22 + parsed_length):])
                value[parsed_length] = result
                parsed_length += result['processed_length']
            parsed_length = (22 + parsed_length)
        else:
            expected_results = int(current_string[7:(7 + 11)], 2)
            parsed_length = 0
            for x in range(expected_results):
                result = parse_packet(current_string[(18 + parsed_length):])
                value[parsed_length] = result
                parsed_length += result['processed_length']
            parsed_length = (18 + parsed_length)
        # parsed_length = round((18 + parsed_length) / 4) * 4
        results = {'packet_version': packet_version,
                   'packet_type': packet_type,
                   'packet_length': packet_length,
                   'expected_results': expected_results,
                   'processed_length': parsed_length,
                   'value': value,}
        return results


x = parse_packet(input_string)

# test_string = 'A0016C880162017C3686B18A3D4780'
# x = parse_packet(bin(int(test_string, 16)).replace('0b', '').zfill(len(test_string) * 4))


print(sum(versions))
