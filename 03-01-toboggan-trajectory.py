def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line.strip()


def count_trees(input, slope):
    x, y = slope
    tree_count = 0
    current_x = 0
    for current_y, line in enumerate(input):
        # print(len(line), line, line[current_x], (current_x, current_y), tree_count)
        if current_y % y == 0 and line[current_x] == '#':
            tree_count += 1
        current_x = (current_x + x) % len(line)
    return tree_count


def test(tests):
    for (t, slope, expected) in tests:
        print((t, slope, expected), count_trees(parse_file(t), slope))
        assert count_trees(parse_file(t), slope) == expected

tests = [("03-01-test_input.txt", (3, 1), 7)]

test(tests)

count = count_trees(parse_file(("03-01-input.txt")), (3, 1))
print("solution:", count)
