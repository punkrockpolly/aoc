def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


def do_things(data):
    return [int(line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'),
            2) for line in data]


def main(seats):
    seats.sort()

    for i, j in enumerate(seats, seats[0]):
        if i != j:
            return i


def test(test_input, expected):
    for pp, expected_valid in zip(test_input, expected):
        is_valid = do_things(pp)
        # print(pp, is_valid, expected_valid)
        assert is_valid == expected_valid


test(parse_file("06-01-test-input.txt"), 
     [False, False, False, False, True, True, True, True])


seats = main(parse_file("06-01-input.txt"))
print("solution:", main(seats))
