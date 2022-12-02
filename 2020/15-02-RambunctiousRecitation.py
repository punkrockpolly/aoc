from collections import OrderedDict

import pytest


def main(puzzle_input, target_turn):
    """seen = {num: last_turn_seen, ...}"""
    seen = OrderedDict((k, v) for v, k in enumerate(puzzle_input, 1))
    turn = len(seen)
    number, turn = seen.popitem()
    while turn < target_turn:
        if number in seen:
            next_number = turn - seen[number]
        else:
            next_number = 0
        seen[number] = turn
        number = next_number
        turn += 1
    return number


TEST_INPUT = [([0, 3, 6], 175594),
              ([1, 3, 2], 2578),
              ([2, 1, 3], 3544142),
              ([1, 2, 3], 261214),
              ([2, 3, 1], 6895259),
              ([3, 2, 1], 18),
              ([3, 1, 2], 362),
              ]


@pytest.mark.parametrize("puzzle_input, expected", TEST_INPUT)
def test(puzzle_input, expected):
    test_results = []
    solution = main(puzzle_input, 30000000)
    test_results.append((puzzle_input, solution, expected))
    assert solution == expected


PUZZLE_INPUT = [12, 1, 16, 3, 11, 0]

number = main(PUZZLE_INPUT, 30000000)
print("solution:", number)
