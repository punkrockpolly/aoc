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


def parse_deck(cards):
    return [int(line) for line in cards.strip().splitlines()[1:]]


def take_turn(player1, player2):
    if player1[0] > player2[0]:
        player1 = player1[1:] + [player1[0], player2[0]]
        player2 = player2[1:]
    else:
        player2 = player2[1:] + [player2[0], player1[0]]
        player1 = player1[1:]

    return (player1, player2)


def calc_score(deck):
    deck.reverse()
    return sum([n * card for n, card in enumerate(deck, 1)])


def main(puzzle_input):
    player1 = parse_deck(next(puzzle_input))
    player2 = parse_deck(next(puzzle_input))

    while player1 and player2:
        player1, player2 = take_turn(player1, player2)

    print("found winner!", player1 or player2)
    winner = player1 or player2
    score = calc_score(winner)
    print(score)
    return score


assert main(parse_file("22-01-test-input.txt")) == 306

score = main(parse_file("22-01-input.txt"))
print("solution:", score)
