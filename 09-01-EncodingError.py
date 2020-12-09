def parse_file(input):
    with open(input) as file:
        for line in file:
            yield int(line)


def is_valid(data, target_num):
    sum_set = set()
    for a in data:
        b = target_num - a
        if b in sum_set:
            return True
        sum_set.add(a)
    return False


def first_invalid(data, preamble):
    current_data = []
    for i, num in enumerate(data):
        if i > preamble:
            if is_valid(current_data[-preamble:], num) is False:
                return num
        current_data.append(num)


def test(test_input, expected):
    invalid_num = first_invalid(test_input, preamble=5)
    print("invalid_num:", invalid_num, "expected:", expected)
    assert invalid_num == expected


test(parse_file("09-01-test-input.txt"), 127)


first_invalid = first_invalid(parse_file("09-01-input.txt"), preamble=25)
print("solution:", first_invalid)
