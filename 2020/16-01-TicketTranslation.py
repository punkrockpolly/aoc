""""
The rules for ticket fields specify a list of fields that exist somewhere on the ticket
and the valid ranges of values for each field.

Adding together all of the invalid values produces your ticket scanning error rate.
"""


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


def parse_rules(puzzle_input):
    ticket_rules = {}
    for line in puzzle_input.strip().splitlines():
        rule, ranges = line.split(': ')
        range1, range2 = ranges.split(' or ')
        start1, end1 = range1.split('-')
        start2, end2 = range2.split('-')
        ticket_rules[rule] = [(int(start1), int(end1) + 1), (int(start2), int(end2) + 1)]
    return ticket_rules


def parse_ticket(puzzle_input):
    for line in puzzle_input.strip().splitlines():
        if 'ticket' not in line:
            yield [int(n) for n in line.split(',')]


def is_valid(value, ticket_rules):
    for rule in ticket_rules.values():
        if value in range(*rule[0]) or value in range(*rule[1]):
            return True
    return False


def sum_invalid_values(puzzle_input):
    ticket_rules = parse_rules(next(puzzle_input))
    ticket = parse_ticket(next(puzzle_input))
    nearby_tickets = parse_ticket(next(puzzle_input))
    scanning_error = 0

    for t in nearby_tickets:
        for value in t:
            if not is_valid(value, ticket_rules):
                scanning_error += value
    return scanning_error


TEST_INPUT = (parse_file("16-01-test-input.txt"), 71)


def test(test_input):
    puzzle_input, expected = test_input
    solution = sum_invalid_values(puzzle_input)

    print('solution:', solution,
          'expected:', expected,
          ('failed', expected - solution) if solution != expected else '')


test(TEST_INPUT)


scanning_error_rate = sum_invalid_values(parse_file("16-01-input.txt"))
print("solution:", scanning_error_rate)
