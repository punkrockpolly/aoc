import copy
import itertools
from collections import defaultdict


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


def parse_line(line):
    i = 0
    while i < len(line):
        if line[i] in ['n', 's']:
            yield line[i] + line[i + 1]
            i += 2
        else:
            yield line[i]
            i += 1


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbors(self):
        return [n + self for n in AXIAL_COORDINATES.values()]

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Position(x=%d, y=%d)" % (self.x, self.y)


AXIAL_COORDINATES = {
    'w': Position(-1, 0),
    'nw': Position(0, -1),
    'ne': Position(1, -1),
    'e': Position(1, 0),
    'se': Position(0, 1),
    'sw': Position(-1, 1),
}


def take_turn(grid):
    """
    Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    """
    updated_grid = copy.deepcopy(grid)

    for (x, y) in itertools.product(range(-75, 75), range(-75, 75)):
        tile = grid[(x, y)]
        neighbors = Position(x, y).get_neighbors()

        neighbors_count = sum([grid[(n.x, n.y)] == 'X' for n in neighbors])
        if tile == 'X' and (neighbors_count not in [1, 2]):
            updated_grid[(x, y)] = ' '
        elif tile == ' ' and neighbors_count == 2:
            updated_grid[(x, y)] = 'X'
    return updated_grid


def count_black_tiles(tile_map):
    return sum([tile == 'X' for tile in tile_map.values()])


def main(puzzle_input, turns):
    # Setup starting grid based on input.
    grid = defaultdict(lambda: ' ')
    for line in puzzle_input:
        current_coord = Position(0, 0)
        for direction in parse_line(line.strip()):
            current_coord += AXIAL_COORDINATES[direction]
        if (current_coord.x, current_coord.y) in grid:
            grid[(current_coord.x, current_coord.y)] = ' '
        else:
            grid[(current_coord.x, current_coord.y)] = 'X'

    # Take turns flipping tiles
    for t in range(turns):
        grid = take_turn(grid)

    return count_black_tiles(grid)

assert main(parse_file("24-01-test-input.txt"), 100) == 2208

tiles = main(parse_file("24-01-input.txt"), 100)
print("solution:", tiles)
