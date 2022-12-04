from itertools import islice


def parse_file(input):
    output = ""
    with open(input) as file:
        for line in file:
            output += line
    return output

def parse_line(line):
    return line.split(',')

def parse_range(r):
    pairs = r.split('-')
    start = int(pairs[0])
    end = int(pairs[1]) + 1
    return range(start, end)

def compare_ranges(r_1, r_2):
    first = set((r_1)).issubset(r_2)
    second = set((r_2)).issubset(r_1)
    return first or second

def find_overlapping_ranges(ranges, compare):
    """returns list of assignment pairs where a range fully contains the other"""
    count = 0
    for r in ranges:
        r_1 = parse_range(r[0])
        r_2 = parse_range(r[1])
        if compare(r_1, r_2):
            count += 1
    return count

def main_1(puzzle_input):
    """how many assignment pairs does one range fully contain the other"""
    lines = puzzle_input.splitlines()
    ranges = [parse_line(line) for line in lines]
    overlaps = find_overlapping_ranges(ranges, compare_ranges)
    return overlaps

def compare_ranges_2(r_1, r_2):
    return set(r_1) & set(r_2)

def main_2(puzzle_input):
    """how many assignment pairs do the ranges overlap"""
    lines = puzzle_input.splitlines()
    ranges = [parse_line(line) for line in lines]
    overlaps = find_overlapping_ranges(ranges, compare_ranges_2)
    return overlaps

TEST_DATA = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

TEST_INPUT_1 = [(TEST_DATA, 2)]
TEST_INPUT_2 = [(TEST_DATA, 4)]

def test(test_input, f):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = f(puzzle_input)
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print('input:', puzzle_input,
              'solution:', solution,
              'expected:', expected,
              ('failed', expected - solution) if solution != expected else '')

test(TEST_INPUT_1, main_1)
solve = main_1(parse_file("inputs/04-Camp-Cleanup.txt"))
print("solution:", solve)

test(TEST_INPUT_2, main_2)
solve = main_2(parse_file("inputs/04-Camp-Cleanup.txt"))
print("solution:", solve)
