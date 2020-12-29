from collections import deque


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield "".join(line.split())  # remove all whitespace


def solve(chars):
    """1+(2*3)+(4*(5+6))"""
    result = 0
    multiplier = 1

    while chars:
        char = chars.popleft()

        if char.isdigit():
            result += multiplier * int(char)
        elif char == '*':
            multiplier = result
            result = 0
        elif char == '(':
            result += multiplier * solve(chars)
        elif char == ')':
            break

    return result


def main(expressions):
    return sum([solve(deque(expr)) for expr in expressions])


TEST_INPUT = [('1 + 2 * 3 + 4 * 5 + 6', 231),
              ('1 + (2 * 3) + (4 * (5 + 6))', 51),
              ('2 * 3 + (4 * 5)', 46),
              ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
              ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
              ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340)
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
