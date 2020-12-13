from collections import defaultdict


def parse_file(input):
    with open(input) as file:
        text = file.read()
        return text.splitlines()


def add_neighbors(x, y, invalid_neighbors):
    neighbors = []
    if 'up' not in invalid_neighbors:
        neighbors.append((x, y - 1))
    if 'down' not in invalid_neighbors:
        neighbors.append((x, y + 1))
    if 'right' not in invalid_neighbors:
        neighbors.append((x + 1, y))
        if 'up' not in invalid_neighbors:
            neighbors.append((x + 1, y - 1))
        if 'down' not in invalid_neighbors:
            neighbors.append((x + 1, y + 1))
    if 'left' not in invalid_neighbors:
        neighbors.append((x - 1, y))
        if 'up' not in invalid_neighbors:
            neighbors.append((x - 1, y - 1))
        if 'down' not in invalid_neighbors:
            neighbors.append((x - 1, y + 1))
    return neighbors


def get_neighbors(layout):
    neighbors = defaultdict(list)
    num_lines = len(layout)
    len_line = len(layout[0])
    for y, line in enumerate(layout):
        for x, position in enumerate(line):
            invalid_neighbors = set()
            if y + 1 >= num_lines:
                invalid_neighbors.add('down')
            if y - 1 < 0:
                invalid_neighbors.add('up')
            if x + 1 >= len_line:
                invalid_neighbors.add('right')
            if x - 1 < 0:
                invalid_neighbors.add('left')
            neighbors[(x, y)] = add_neighbors(x, y, invalid_neighbors)
    return neighbors


def update_seat(x, y, position, layout, result_layout, neighbors, updated):
    """
    floor (.), an empty seat (L), or an occupied seat (#)

    If a seat is empty (L) and there are no occupied seats adjacent to it,
        the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied,
        the seat becomes empty.
    Otherwise, the seat's state does not change.
    """
    if position == 'L':
        if all(layout[ny][nx] in ['L', '.'] for (nx, ny) in neighbors[(x, y)]):
            result_layout[y] = result_layout[y][:x] + '#' + result_layout[y][x + 1:]
            if layout[y][x] != '#':
                updated = True
    if position == '#':
        occupied_neighbors = len(list(1 for (nx, ny) in neighbors[(x, y)] if layout[ny][nx] == '#'))
        if occupied_neighbors >= 4:
            result_layout[y] = result_layout[y][:x] + 'L' + result_layout[y][x + 1:]
            if layout[y][x] != 'L':
                updated = True
    return (result_layout, updated)


def apply_seating_round(layout, neighbors):
    updated = False
    result_layout = layout.copy()
    for y, line in enumerate(layout):
        for x, position in enumerate(line):
            result_layout, updated = update_seat(x, y, position, layout, result_layout, neighbors, updated)

    # print(result_layout)
    return result_layout, updated


def main(layout):
    neighbors = get_neighbors(layout)
    updated = True
    turn = 0
    while updated:
        turn += 1
        layout, updated = apply_seating_round(layout, neighbors)
    return ''.join(layout).count('#')


def test(test_input, expected):
    result = main(test_input)
    print('expected:', expected, 'result', result)
    assert result == expected

test_input = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

test(test_input.splitlines(), 37)


seats = main(parse_file("11-01-input.txt"))
print("solution:", seats)
