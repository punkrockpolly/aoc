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
        if current_y % y != 0:
            continue
        if line[current_x] == '#':
            tree_count += 1
        current_x = (current_x + x) % len(line)
    return tree_count


def test(slopes, expected):
    for slope, result in zip(slopes, expected):
        test_input = parse_file("03-01-test_input.txt")
        tree_count = count_trees(test_input, slope)
        # print((n, slope, result, tree_count)
        assert tree_count == result

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
expected = [2, 7, 3, 4, 2]

test(slopes, expected)

product = 1

for slope in slopes:
    count = count_trees(parse_file("03-01-input.txt"), slope)
    product *= count
print("solution:", product)
