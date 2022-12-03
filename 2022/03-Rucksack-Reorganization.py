from itertools import islice


def parse_file(input):
    output = ""
    with open(input) as file:
        for line in file:
            output += line
    return output

def get_priority(item):
    """
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    """
    if item.lower() == item:
        return ord(item) - 96
    return ord(item) - 38

def find_item(backpack):
    """Return char found in both compartments"""
    compartment_1, compartment_2 = backpack
    return (set(compartment_1) & set(compartment_2)).pop()

def unpack(line):
    """
    The list of items for each rucksack is given as characters all on a single line. 
    The first half of the characters represent items in the first compartment, 
    while the second half of the characters represent items in the second compartment.
    
    return tuple
    """
    compartment_size = len(line)//2
    return (line[:compartment_size], line[compartment_size:])

def main_1(puzzle_input):
    """
    Your total score is the sum of your scores for each round. 
    """
    lines = puzzle_input.splitlines()
    backpacks = [unpack(line) for line in lines]
    return sum([get_priority(item) for backpack in backpacks for item in find_item(backpack)]) 

def find_badge(group):
    backpack_1, backpack_2, backpack_3 = group
    return (set(backpack_1) & set(backpack_2) & set(backpack_3)).pop()

def build_groups(lines):
    """group every 3"""
    return zip(*[iter(lines)] * 3)

def main_2(puzzle_input):
    """
    Your total score is the sum of your scores for each round. 
    """
    lines = puzzle_input.splitlines()
    groups = build_groups(lines)
    return sum([get_priority(item) for group in groups for item in find_badge(group)]) 

TEST_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

TEST_INPUT_1 = [(TEST_DATA, 157)]

TEST_INPUT_2 = [(TEST_DATA, 70)]

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
test(TEST_INPUT_2, main_2)

solve = main_2(parse_file("inputs/03-Rucksack-Reorganization.txt"))
print("solution:", solve)
