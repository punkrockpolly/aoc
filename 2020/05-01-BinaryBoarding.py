def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


def binary_space_partition(data):
    highest = 0
    for line in data:
        binary = line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
        highest = max(highest, int(binary, 2))
    return highest


def test(test_input, expected):
    assert binary_space_partition(test_input) == expected


test(parse_file("05-01-test-input.txt"), 820)

highest = binary_space_partition(parse_file("05-01-input.txt"))
print("solution:", highest)
