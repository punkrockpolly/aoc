from collections import deque
from operator import add, mul


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield "".join(line.split())  # remove all whitespace


def solve(chars):
    """1+(2*3)+(4*(5+6))"""
    result = 0
    op = add

    while chars:
        char = chars.popleft()

        if char.isdigit():
            result = op(result, int(char))
        elif char == '+':
            op = add
        elif char == '*':
            op = mul
        elif char == '(':
            result = op(result, solve(chars))
        elif char == ')':
            break

    return result


def main(expressions):
    return sum([solve(deque(expr)) for expr in expressions])


TEST_INPUT = [('1 + 2 * 3 + 4 * 5 + 6', 71),
              ('1 + (2 * 3) + (4 * (5 + 6))', 51),
              ('2 * 3 + (4 * 5)', 26),
              ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
              ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
              ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632)
              ]


def test(test_input):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = solve(deque("".join(puzzle_input.split())))
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print(puzzle_input,
              'solution:', solution,
              'expected:', expected,
              ('failed', expected - solution) if solution != expected else '')


test(TEST_INPUT)

homework_sum = main(parse_file("18-01-input.txt"))
print("solution:", homework_sum)
