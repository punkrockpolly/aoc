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

Goal: At the end of these instructions, the ship's Manhattan distance
(sum of the absolute values of its east/west position and its north/south position)
from its starting position is 17 + 8 = 25.
"""


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


class Ferry():
    def __init__(self, starting_degrees):
        self.degrees_to_direction = {
            0: 'north',
            90: 'east',
            180: 'south',
            270: 'west',
        }
        self.current_degrees = starting_degrees
        self.current_direction = self.degrees_to_direction[starting_degrees]
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
            self.turn(action, value)
        else:
            self.move(action, value)

    def move(self, direction, distance):
        if direction == 'front':
            direction = self.current_direction
        if direction in ['south', 'west']:
            distance *= -1

        to_update = 'north_value' if direction in ['north', 'south'] else 'east_value'
        self.manhattan_distance[to_update] += distance

    def turn(self, direction, degrees):
        """
        Rotate waypoint around the ship the given degrees.

        A waypoint starts at 10 units east and 4 units north
        R90 rotates the waypoint around the ship clockwise 90 degrees,
        moving it to 4 units east and 10 units south
        """
        if direction == 'left':  # counter-clockwise
            degrees *= -1
        else:  # clockwise
            pass
        self.current_degrees += degrees
        self.current_direction = self.degrees_to_direction[self.current_degrees % 360]

    def get_manhattan_distance(self):
        return abs(self.manhattan_distance['north_value']) + abs(self.manhattan_distance['east_value'])


def main(puzzle_input):
    ferry = Ferry(90)
    actions = {
        'N': 'north',
        'S': 'south',
        'E': 'east',
        'W': 'west',
        'L': 'left',
        'R': 'right',
        'F': 'front',
    }
    for nav_instruction in puzzle_input:
        action = actions[nav_instruction[0]]
        value = int(nav_instruction[1:])
        ferry.run_action(action, value)
        # print(action, value, ferry.manhattan_distance, ferry.current_direction)
    return ferry.get_manhattan_distance()

TEST_INPUT = [("""\
F10
N3
F7
R90
F11""", 25), ]


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
