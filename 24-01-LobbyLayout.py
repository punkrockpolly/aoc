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

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Position(x=%d, y=%d)" % (self.x, self.y)


def main(puzzle_input):
    axial_coordinates = {
        'w': Position(-1, 0),
        'nw': Position(0, -1),
        'ne': Position(1, -1),
        'e': Position(1, 0),
        'se': Position(0, 1),
        'sw': Position(-1, 1),
    }
    tile_grid = []
    for line in puzzle_input:
        current_coord = Position(0, 0)
        for direction in parse_line(line.strip()):
            current_coord += axial_coordinates[direction]
        if current_coord in tile_grid:
            tile_grid.remove(current_coord)
        else:
            tile_grid.append(current_coord)
    return (len(tile_grid))

assert main(parse_file("24-01-test-input.txt")) == 10

tiles = main(parse_file("24-01-input.txt"))
print("solution:", tiles)
