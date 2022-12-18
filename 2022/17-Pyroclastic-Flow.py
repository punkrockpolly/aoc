from collections import defaultdict

minus = [
    list("####")
]
plus = [
    list(".#."),
    list("###"),
    list(".#."),
]

j = [
    list("..#"),
    list("..#"),
    list("###"),
][::-1]

l = [
    ["#"], ["#"], ["#"], ["#"]
]

square = [
    list("##"),
    list("##")
]

shapes = [minus, plus, j, l, square]


class grid:
    def __init__(self, pattern):
        self.data = set()
        self.top = 0
        self.current_shape_idx = 0
        self.shape_x = 2
        self.shape_y = 3
        self.settled = 0
        self.pattern = pattern
        self.pat_idx = 0

    def can_move_horizontal(self, direction):
        if direction == "<":
            nx = self.shape_x - 1
        else:
            nx = self.shape_x + 1

        if nx in [-1, 7]:
            return False

        for y, l in enumerate(shapes[self.current_shape_idx]):
            for x, c in enumerate(l):
                if c == "#":
                    if (nx + x, self.shape_y + y) in self.data or nx + x > 6:
                        return False
        return True

    def can_move_down(self):
        ny = self.shape_y - 1

        if ny < 0:
            return False

        for y, l in enumerate(shapes[self.current_shape_idx]):
            for x, c in enumerate(l):
                if c == "#":
                    if (self.shape_x + x, ny + y) in self.data:
                        return False
        return True

    def move(self):
        direction = self.pattern[self.pat_idx % len(self.pattern)]
        self.pat_idx = self.pat_idx + 1

        if self.can_move_horizontal(direction):
            if direction == "<":
                self.shape_x -= 1
            else:
                self.shape_x += 1

        if self.can_move_down():
            self.shape_y -= 1
        else:
            return True

        return False

    def drop(self):
        while True:
            ret = self.move()
            if ret:
                break

        self.draw()

    def get_top(self):
        return max(c[1] for c in self.data)

    def draw(self):
        for y, l in enumerate(shapes[self.current_shape_idx]):
            for x, c in enumerate(l):
                if c == "#":
                    self.data.add((self.shape_x + x, self.shape_y + y))

        self.settled += 1
        self.top = self.get_top()
        self.current_shape_idx = (self.current_shape_idx + 1) % 5
        self.shape_x = 2
        self.shape_y = self.top + 3 + 1

    def plot(self):
        buff = []
        for y in range(100):
            st = ""
            for x in range(7):
                st += "#" if (x, y) in self.data else "."
            buff.append(st)

        for l in buff[::-1]:
            print(l)

    def find_pattern(self):
        states = defaultdict(list)
        heights = {}

        while True:
            self.drop()
            top = self.get_top()

            heights[self.settled] = top + 1

            if all((x, top) in self.data for x in range(7)):
                s = (self.pat_idx % len(self.pattern), self.current_shape_idx)
                states[s].append(self.settled)
                if len(states[s]) == 2:
                    return states[s], heights


def main_1(puzzle_input):
    turns = 2022
    g = grid(puzzle_input)

    for _ in range(turns):
        g.drop()

    return g.get_top() + 1


def main_2(puzzle_input):
    turns = 1000000000000
    g = grid(puzzle_input)

    pt, heights = g.find_pattern()

    initial_height = heights[min(pt)]

    cycles = (turns - min(pt)) // (max(pt) - min(pt))
    cycle_height = heights[max(pt)] - heights[min(pt)]

    extra_rocks = (turns - max(pt)) % (max(pt) - min(pt))
    extra_height = heights[min(pt) + extra_rocks] - heights[min(pt)]

    return initial_height + cycles * cycle_height + extra_height

TEST_INPUT_1 = [('>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>', 3068),
]

def test(test_input, f):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = f(puzzle_input)
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:
        print('input:', puzzle_input,
              '\nsolution:', solution,
              'expected:', expected,
              ('failed') if solution != expected else '')

test(TEST_INPUT_1, main_1)
solve = main_1(open("inputs/17-Pyroclastic-Flow.txt").read())
print("part 1 solution:", solve)

solve = main_2(open("inputs/17-Pyroclastic-Flow.txt").read())
print("part 2 solution:", solve)
