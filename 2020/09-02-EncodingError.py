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


def find_range(data, target_num):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if sum(data[i:j]) == target_num:
                print("range:", data[i:j])
                return sum([min(data[i:j]), max(data[i:j])])


def test(test_input, expected):
    invalid_num = first_invalid(test_input, preamble=5)
    solution = find_range(test_input, invalid_num)
    print("solution:", solution, "expected:", expected)
    assert solution == solution


parsed_input = list(parse_file("09-01-test-input.txt"))
test(parsed_input, 62)


parsed_input = list(parse_file("09-01-input.txt"))
first_invalid = first_invalid(parsed_input, preamble=25)
print("first_invalid:", first_invalid)
solution = find_range(parsed_input, first_invalid)
print("solution:", solution)
