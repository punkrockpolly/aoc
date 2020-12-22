"""
The navigation instructions (your puzzle input) consists of
a sequence of single-character [actions] paired with [integer] input values.

0° corresponds to north,
90° angle corresponds to east,
180° angle to south,
270° to west

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.

Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship.
Forward moves the ship to the waypoint 10 times the value.

Goal: Find Manhattan distance from ships starting position.

solution: 562 too low

"""


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


class Ferry():
    def __init__(self):
        self.manhattan_distance = {
            'north_value': 0,
            'east_value': 0
        }
        self.waypoint = {
            'north_value': 1,
            'east_value': 10
        }

    def run_action(self, action, value):
        if action in ['left', 'right']:
            turns = int(value / 90)
            for n in range(turns):
                self.turn(action)
        elif action == 'forward':
            self.move_forward(value)
        else:
            self.move_waypoint(action, value)

    def move_waypoint(self, direction, distance):
        if direction in ['south', 'west']:
            distance *= -1

        to_update = 'north_value' if direction in ['north', 'south'] else 'east_value'
        self.waypoint[to_update] += distance

    def move_forward(self, value):
        """Move forward to the waypoint a number of times equal to the given value."""
        self.manhattan_distance['north_value'] += (value * self.waypoint['north_value'])
        self.manhattan_distance['east_value'] += (value * self.waypoint['east_value'])

    def turn(self, direction):
        """
        Rotate waypoint around the ship the given degrees.

        A waypoint starts at 10 units east and 4 units north
        R90 rotates the waypoint around the ship clockwise 90 degrees,
        moving it to 4 units east and 10 units south
        """
        value = -1 if direction == 'left' else 1

        north_value = (value * -self.waypoint['east_value'])
        east_value = (value * self.waypoint['north_value'])
        self.waypoint['north_value'] = north_value
        self.waypoint['east_value'] = east_value

    def get_manhattan_distance(self):
        return abs(self.manhattan_distance['north_value']) + abs(self.manhattan_distance['east_value'])


def main(puzzle_input):
    ferry = Ferry()
    actions = {
        'N': 'north',
        'S': 'south',
        'E': 'east',
        'W': 'west',
        'L': 'left',
        'R': 'right',
        'F': 'forward',
    }
    for nav_instruction in puzzle_input:
        action = actions[nav_instruction[0]]
        value = int(nav_instruction[1:])
        ferry.run_action(action, value)
    return ferry.get_manhattan_distance()

TEST_INPUT = [("""\
F10
N3
F7
R90
F11""", 286), ]


def test(test_input):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = main(puzzle_input.splitlines())
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:
        print(puzzle_input,
              'solution:', solution,
              'expected:', expected,
              ('failed', expected - solution) if solution != expected else '')


test(TEST_INPUT)


manhattan_distance = main(parse_file("12-01-input.txt"))
print("solution:", manhattan_distance)
