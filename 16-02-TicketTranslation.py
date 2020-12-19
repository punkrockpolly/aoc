""""
Once you work out which field is which,
look for the six fields on your ticket that start with the word departure.

What do you get if you multiply those six values together?
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
        print(rule[0], rule[1], value)
        if value in range(*rule[0]) or value in range(*rule[1]):
            return True
    return False


def departure_fields(puzzle_input):
    ticket_rules = parse_rules(next(puzzle_input))
    ticket = parse_ticket(next(puzzle_input))
    nearby_tickets = parse_ticket(next(puzzle_input))

    valid_tickets = []
    for t in nearby_tickets:
        if all(is_valid(value, ticket_rules) for value in t):
            valid_tickets.append(t)
    print(len(valid_tickets))

scanning_error_rate = departure_fields(parse_file("16-01-input.txt"))
print("solution:", scanning_error_rate)
