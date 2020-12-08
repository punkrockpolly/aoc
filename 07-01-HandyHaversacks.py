from collections import defaultdict


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


def build_bag_graph(data):
    bag_graph = defaultdict(dict)
    for rule in data:
        # light red bags contain 1 bright white bag, 2 muted yellow bags.
        bag_color, contents = rule.split(" bags contain ")
        for c in contents.split(", "):
            # contents = '1 bright white bag, 2 muted yellow bags.'
            # c = '1 bright white bag'
            count = c[0]
            color = c[2:c.find(' bag')]
            bag_graph[bag_color][color] = count
    return bag_graph

"""
bag_graph = {
'light red': {'bright white': '1', 'muted yellow': '2'},
'dark orange': {'bright white': '3', 'muted yellow': '4'},
'bright white': {'shiny gold': '1'},
'muted yellow': {'shiny gold': '2', 'faded blue': '9'},
'shiny gold': {'dark olive': '1', 'vibrant plum': '2'},
'dark olive': {'faded blue': '3', 'dotted black': '4'},
'vibrant plum': {'faded blue': '5', 'dotted black': '6'},
'faded blue': {' other': 'n'},
'dotted black': {' other': 'n'}}
"""


def count_bags(bag_graph, color):
    """How many different bag colors would be valid for the outermost bag?"""
    outermost_graph = defaultdict(list)
    for outer_color, contents in bag_graph.items():
        # light red {'bright white': '1', 'muted yellow': '2'}
        for inner_color in contents:
            outermost_graph[inner_color].append(outer_color)
    """
    outermost_graph = {
    'bright white': ['light red', 'dark orange'],
    'muted yellow': ['light red', 'dark orange'],
    'shiny gold': ['bright white', 'muted yellow'],
    'faded blue': ['muted yellow', 'dark olive', 'vibrant plum'],
    'dark olive': ['shiny gold'],
    'vibrant plum': ['shiny gold'],
    'dotted black': ['dark olive', 'vibrant plum'],
    ' other': ['faded blue', 'dotted black']}
    """

    def _count_outer_bags(target_color):
        outer_colors = set()
        stack = [target_color]
        while stack:
            color = stack.pop()
            for parent_bag in outermost_graph[color]:
                """['pale purple', 'vibrant coral', 'dotted fuchsia']"""
                if parent_bag not in outer_colors:
                    outer_colors.add(parent_bag)
                    stack.append(parent_bag)
        return len(outer_colors)

    return _count_outer_bags(color)



def test(test_input, expected):
    bag_graph = build_bag_graph(test_input)
    count = count_bags(bag_graph, 'shiny gold')
    print("count:", count, "expected:", expected)
    assert count == expected


test(parse_file("07-01-test-input.txt"), 4)


bags = build_bag_graph(parse_file("07-01-input.txt"))
print("solution:", count_bags(bags, 'shiny gold'))
