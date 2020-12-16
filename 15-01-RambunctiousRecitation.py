import pytest


def main(puzzle_input, target_turn):
    seen = list(puzzle_input)
    turn = len(seen)
    while turn <= target_turn:
        number = seen.pop()
        if number in seen:
            seen.extend([number, turn - 1 - next(
                i for i in reversed(
                    range(len(seen))) if seen[i] == number)])
        else:
            seen.extend([number, 0])
        turn += 1
    return number


TEST_INPUT = [([0, 3, 6], 436),
              ([1, 3, 2], 1),
              ([2, 1, 3], 10),
              ([1, 2, 3], 27),
              ([2, 3, 1], 78),
              ([3, 2, 1], 438),
              ([3, 1, 2], 1836),
              ]


@pytest.mark.parametrize("puzzle_input, expected", TEST_INPUT)
def test(puzzle_input, expected):
    test_results = []
    solution = main(puzzle_input, 2020)
    test_results.append((puzzle_input, solution, expected))
    assert solution == expected


PUZZLE_INPUT = [12, 1, 16, 3, 11, 0]

number = main(PUZZLE_INPUT, 2020)
print("solution:", number)
