"""
Find the earliest timestamp such that
the first bus ID departs at that time and
each subsequent listed bus ID departs at that subsequent minute.

An x in the schedule means there are no constraints
"""
from math import gcd

TEST_INPUT = [([7, 13, 'x', 'x', 59, 'x', 31, 19], 1068781),
              ([17, 'x', 13, 19], 3417),
              ([67, 7, 59, 61], 754018),
              ([67, 'x', 7, 59, 61], 779210),
              ([67, 7, 'x', 59, 61], 1261476),
              ([1789, 37, 47, 1889], 1202161486)
              ]
PUZZLE_INPUT = [13, 'x', 'x', 41, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 467, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x', 'x', 17, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 29, 'x', 353, 'x', 'x', 'x', 'x', 'x', 37, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 23]


def lcm(a, b):
    """Compute the lowest common multiple of a and b."""
    return abs(a * b) // gcd(a, b)


def find_timestamp(puzzle_input):
    timestamp = 0
    bus_ids = [(i, bus_id) for i, bus_id in enumerate(puzzle_input) if bus_id != 'x']
    remaining = len(bus_ids)
    increment = bus_ids[0][1]
    while remaining:
        minutes, bus_id = bus_ids[len(bus_ids) - remaining]
        if (timestamp + minutes) % bus_id == 0:
            increment = lcm(increment, bus_id)
            remaining -= 1
        else:
            timestamp += increment
    return timestamp


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
print("solution:", find_timestamp(PUZZLE_INPUT))
