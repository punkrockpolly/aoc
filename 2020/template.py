def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


def do_things(data):
    return [int(line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'),
            2) for line in data]


def main(puzzle_input):
    seats.sort()

    for i, j in enumerate(seats, seats[0]):
        if i != j:
            return i

TEST_INPUT = [([7, 13, 'x', 'x', 59, 'x', 31, 19], 1068781),
              ([17, 'x', 13, 19], 3417),
              ([67, 7, 59, 61], 754018),
              ([67, 'x', 7, 59, 61], 779210),
              ([67, 7, 'x', 59, 61], 1261476),
              ([1789, 37, 47, 1889], 1202161486)
              ]


def test(test_input):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = find_timestamp(puzzle_input)
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print(puzzle_input,
              'solution:', solution,
              'expected:', expected,
              ('failed', expected - solution) if solution != expected else '')


test(TEST_INPUT)


seats = main(parse_file("06-01-input.txt"))
print("solution:", seats)
