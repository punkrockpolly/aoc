def parse_file(input):
    output = ""
    with open(input) as file:
        for line in file:
            output += line
    return output

def score_round(line):
    """
    The first column is what your opponent is going to play: 
    A for Rock, B for Paper, and C for Scissors.

    The second column says how the round needs to end: 
    X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    """
    mapping = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
    }
    opp = mapping[line[0]]
    outcome = mapping[line[2]]
    play = determine_play(opp, outcome)

    print(f'line: {line} -> {opp} {play}')
    return get_shape_score(play) + get_outcome_score(opp, play)

def determine_play(opp, outcome):
    if outcome == 'draw':
        return opp
    if outcome == 'win':
        if opp == 'rock':
            return 'paper'
        if opp == 'paper':
            return 'scissors'
        if opp == 'scissors':
            return 'rock'
    if outcome == 'lose':
        if opp == 'rock':
            return 'scissors'
        if opp == 'paper':
            return 'rock'
        if opp == 'scissors':
            return 'paper'

def get_outcome_score(opp, play):
    """
    Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Roc
    The score for the outcome of the round.
    (0 if you lost, 3 if the round was a draw, and 6 if you won)
    """
    if opp == play:
        return 3
    if opp == 'rock' and play == 'paper':
        return 6
    if opp == 'rock' and play == 'scissors':
        return 0
    if opp == 'paper' and play == 'rock':
        return 0
    if opp == 'paper' and play == 'scissors':
        return 6
    if opp == 'scissors' and play == 'paper':
        return 0
    if opp == 'scissors' and play == 'rock':
        return 6

def get_shape_score(play):
    """
    The score for a single round is the score for the shape you selected.
    (1 for Rock, 2 for Paper, and 3 for Scissors) 
    """
    shape_score = {
        'rock': 1,
        'paper': 2,
        'scissors': 3,
    }
    return shape_score[play]


def main(puzzle_input):
    """
    Your total score is the sum of your scores for each round. 
    """
    lines = puzzle_input.splitlines()
    return sum(score_round(line) for line in lines)

TEST_INPUT = [("""A Y
B X
C Z""", 12)]


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

solve = main(parse_file("inputs/02-01-Rock-Paper-Scissors.txt"))
print("solution:", solve)
