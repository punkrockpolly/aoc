"""
Puzzle input consist of two lines.
The first line is your estimate of the earliest timestamp you could depart on a bus.
The second line lists the bus IDs that are in service according to the shuttle company;
entries that show x must be out of service, so you decide to ignore them.

goal is to figure out the earliest bus you can take
"""

TEST_EARLIEST_TIMESTAMP = 939
TEST_INPUT = [7,13,'x','x',59,'x',31,19]

EARLIEST_TIMESTAMP = 1008713
PUZZLE_INPUT = [13,'x','x',41,'x','x','x','x','x','x','x','x','x',467,'x','x','x','x','x','x','x','x','x','x','x',19,'x','x','x','x',17,'x','x','x','x','x','x','x','x','x','x','x',29,'x',353,'x','x','x','x','x',37,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',23]


def find_bus(target, puzzle_input):
    best_time = target
    while True:
        for bus_id in puzzle_input:
            if bus_id != 'x' and best_time % int(bus_id) == 0:
                return bus_id * (best_time - target)
        best_time += 1

assert find_bus(TEST_EARLIEST_TIMESTAMP, TEST_INPUT) == 295
print("solution:", find_bus(EARLIEST_TIMESTAMP, PUZZLE_INPUT))
