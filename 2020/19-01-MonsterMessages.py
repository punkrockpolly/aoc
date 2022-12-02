def parse_file(puzzle_input):
    """A very ugly way to yield multiline strings without regex."""
    with open(puzzle_input) as file:
        p = ''
        for line in file:
            p += line
            if line == "\n":
                yield p
                p = ''
        yield p


def parse_rule(rule):
    """
    [4, 1, 5]
    [[2, 3], [3, 2]]
    [[4, 4], [5, 5]]
    [[4, 5], [5, 4]]
    a
    b
    """
    if rule[0] == '"':
        return rule.replace('"', '')
    if '|' in rule:  # 14 92 | 10 110
        rule1, rule2 = rule.split(' | ')
        return [parse_rule(rule1), parse_rule(rule2)]
    return [int(n) for n in rule.split()]


def parse_rules(puzzle_input):
    message_rules = {}
    for line in puzzle_input.strip().splitlines():
        rule_index, rule = line.split(': ')
        message_rules[int(rule_index)] = parse_rule(rule)
    return message_rules


def is_valid(message, rules):
    """If message completely matches rule 0."""
    pass


def main(puzzle_input):
    validation_rules, message = puzzle_input
    message_rules = parse_rules(validation_rules)
    print(message_rules)


TEST_INPUT = (
    """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""", 2)

"""
ababbb and abbbab match,
but bababa, aaabbb, and aaaabbb do not,
producing the answer 2.
"""


def test(test_input):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = main(puzzle_input)
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print(puzzle_input,
              'solution:', solution,
              'expected:', expected,
              ('failed', expected - solution) if solution != expected else '')


# test(parse_file(TEST_INPUT))

PUZZLE_INPUT = "19-01-input.txt"
TEST_INPUT = "19-01-test-input.txt"

count_messages = main(parse_file(TEST_INPUT))
print("solution:", count_messages)
