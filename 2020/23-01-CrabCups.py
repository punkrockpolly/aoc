def move_cups(cups):
    """
    to move: three cups that are immediately clockwise of the current cup
    destination cup: current cup's label minus one
        If this would select one of the cups that was just picked up,
        the crab will keep subtracting one until it finds a cup that wasn't
        just picked up.
        If at any point in this process the value goes below the lowest value
        on any cup's label, it wraps around to the highest value on any cup's label instead.
    place the cups picked up immediately clockwise of the destination cup
    new current cup: the cup which is immediately clockwise of the current cup
    """
    current = cups[0]
    destination = -1
    i = 1
    to_move = cups[1:4]
    cups = cups[4:] + current
    while destination == -1:
        target = str(int(current) - i)
        destination = cups.find(target)
        i += 1
        if i > 9:
            current = '9'
            i = 0

    return cups[:destination + 1] + to_move + cups[destination + 1:]


def main(cups, moves):
    for move in range(moves):
        cups = move_cups(cups)
    cup_1 = cups.find('1')

    return cups[cup_1 + 1:] + cups[:cup_1]


TEST_INPUT = '389125467'
TEST_10_MOVES = '92658374'
TEST_100_MOVES = '67384529'

assert main(TEST_INPUT, 10) == TEST_10_MOVES
assert main(TEST_INPUT, 100) == TEST_100_MOVES


cups = main('624397158', 100)
print("solution:", cups)
