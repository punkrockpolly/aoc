def parse_file(input):
    output = ""
    with open(input) as file:
        for line in file:
            output += line
    return output

def parse_groups(lines):
    group = set()
    # print(f"lines {lines}")
    for line in lines.splitlines():
        # print(f"line {line}")
        if line == "":
            yield group
            group = set()
        else:
            group.add(int(line.strip()))


def main(puzzle_input):
    groups = parse_groups(puzzle_input)
    sums = [sum(group) for group in groups]
    return sum(sorted(sums, reverse=True)[:3])

TEST_INPUT = [("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""", 45000)]


def test(test_input):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = main(puzzle_input)
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print('input:', puzzle_input,
              'solution:', solution,
              'expected:', expected,
              ('failed', expected - solution) if solution != expected else '')


test(TEST_INPUT)


solve = main(parse_file("inputs/01-01-Calorie-Counting.txt"))
print("solution:", solve)
