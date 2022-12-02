from copy import deepcopy


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


class CrabCombat:
    def __init__(self, puzzle_input):
        self.player1 = self.parse_deck(next(puzzle_input))
        self.player2 = self.parse_deck(next(puzzle_input))
        self.seen = set()

    def save_state(self, deck1, deck2):
        return ",".join([str(n) for n in deck1 + ['x'] + deck2])

    def parse_deck(self, cards):
        return [int(line) for line in cards.strip().splitlines()[1:]]

    def take_turn(self, deck1, deck2):
        """Return (winner, (deck1, deck2))."""
        new_state = self.save_state(deck1, deck2)
        # if we've seen this state before, player1 wins
        if new_state in self.seen:
            return (0, (deck1, deck2))

        self.seen.add(new_state)

        # if both players have at least as many cards remaining
        # in their deck as the value of the card they just drew,
        # the winner of the round is determined by playing a new game of Recursive Combat
        if len(deck1) > deck1[0] and len(deck2) > deck2[0]:
            player1 = deck1[1:deck1[0] + 1]
            player2 = deck2[1:deck2[0] + 1]
            winner_idx = None
            new_game = deepcopy(self)
            while winner_idx is None:
                winner_idx, (player1, player2) = new_game.take_turn(player1, player2)
        else:
            winner_idx = 0 if deck1[0] > deck2[0] else 1

        if winner_idx == 0:
            deck1 = deck1[1:] + [deck1[0], deck2[0]]
            deck2 = deck2[1:]
        else:
            deck2 = deck2[1:] + [deck2[0], deck1[0]]
            deck1 = deck1[1:]

        if not (deck1 and deck2):  # one of the decks is empty
            return (0 if deck1 else 1, (deck1, deck2))
        else:
            return (None, (deck1, deck2))


def calc_score(deck):
    deck.reverse()
    return sum([n * card for n, card in enumerate(deck, 1)])


def main(puzzle_input):
    game = CrabCombat(puzzle_input)
    winner_idx = None

    while winner_idx is None:
        winner_idx, (game.player1, game.player2) = game.take_turn(game.player1, game.player2)

    winner = (game.player1, game.player2)[winner_idx]
    print("found winner!", winner)
    score = calc_score(winner)
    print(score)
    return score


assert main(parse_file("22-02-test-input.txt")) == 105
assert main(parse_file("22-01-test-input.txt")) == 291

score = main(parse_file("22-01-input.txt"))
print("solution:", score)
