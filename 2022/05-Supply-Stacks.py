from collections import defaultdict


def parse_input(input):
    stacks, moves = input.split('\n\n')
    return (stacks, moves)

def parse_file(input, is_test=False):
    if is_test:
        return parse_input(input)
    with open(input) as file:
        file_input = ''.join(line for line in file)
        return parse_input(file_input)

def parse_stacks(stacks):
    """parses lines of stacks into a dict of stacks, where the first item is the bottom"""
    parsed_stacks = defaultdict(list)
    for line in stacks.splitlines():
        crates = line[1::4]
        for i, crate in enumerate(crates):
            if crate != ' ':
                parsed_stacks[i].append(crate)
    return {key: stack[::-1][1:] for key, stack in parsed_stacks.items()}

def parse_moves(moves):
    """parse each line into the move instructions"""
    for move in moves.splitlines():
        yield (int(s) for s in move.split() if s.isdigit())

def make_moves(stacks, moves):
    for (n, src, dest) in moves:
        for _ in range(n):
            crate = stacks[src - 1].pop()
            stacks[dest - 1].append(crate)
    return stacks

def make_moves_2(stacks, moves):
    for (n, src, dest) in moves:
        crates = []
        for _ in range(n):
            crates.append(stacks[src - 1].pop())
        crates.reverse()
        stacks[dest - 1].extend(crates)
    return stacks

def get_tops(stacks):
    return "".join([stacks[i][-1] for i in range(len(stacks))])

def main_1(puzzle_input, is_test=False):
    """which crate will end up on top of each stack"""
    stacks, moves = parse_file(puzzle_input, is_test)
    parsed_stacks = parse_stacks(stacks)
    parsed_moves = parse_moves(moves)
    print(f'parsed_stacks: {parsed_stacks}')
    stacks = make_moves(parsed_stacks, parsed_moves)
    top_crates = get_tops(stacks)
    return top_crates

def main_2(puzzle_input, is_test=False):
    """which crate will end up on top of each stack"""
    stacks, moves = parse_file(puzzle_input, is_test)
    parsed_stacks = parse_stacks(stacks)
    parsed_moves = parse_moves(moves)
    print(f'parsed_stacks: {parsed_stacks}')
    stacks = make_moves_2(parsed_stacks, parsed_moves)
    top_crates = get_tops(stacks)
    return top_crates

TEST_DATA = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

TEST_INPUT_1 = [(TEST_DATA, 'CMZ')]
TEST_INPUT_2 = [(TEST_DATA, 'MCD')]

def test(test_input, f):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = f(puzzle_input, True)
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print('input:', puzzle_input,
              '\nsolution:', solution,
              'expected:', expected,
              ('failed') if solution != expected else '')

test(TEST_INPUT_1, main_1)
solve = main_1("inputs/05-Supply-Stacks.txt")
print("solution:", solve)

test(TEST_INPUT_2, main_2)
solve = main_2("inputs/05-Supply-Stacks.txt")
print("solution:", solve)
