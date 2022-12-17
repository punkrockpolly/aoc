def parse_file(input, is_test=False):
    if is_test:
        return input
    with open(input) as file:
        file_input = ''.join(line for line in file)
        return file_input

def detect_start(datastream):
    """
    Detect a start-of-packet marker in the datastream
    The start of a packet is indicated by a sequence of four characters that are all different
    """
    for i in range(3, len(datastream)):
        s = set(datastream[i-3:i+1])
        if len(s) == 4:
            return i + 1

def main_1(puzzle_input, is_test=False):
    """How many characters need to be processed before the first start-of-packet marker is detected?"""
    datastream = parse_file(puzzle_input, is_test)
    return detect_start(datastream)

def detect_start_2(datastream):
    """
    Detect a start-of-packet marker in the datastream
    The start of a packet is indicated by a sequence of 14 characters that are all different
    """
    for i in range(13, len(datastream)):
        s = set(datastream[i-13:i+1])
        if len(s) == 14:
            return i + 1

def main_2(puzzle_input, is_test=False):
    """How many characters need to be processed before the first start-of-packet marker is detected?"""
    datastream = parse_file(puzzle_input, is_test)
    return detect_start_2(datastream)


TEST_INPUT_1 = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
                ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
                ('nppdvjthqldpwncqszvftbrmjlhg', 6),
                ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
                ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
]

TEST_INPUT_2 = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
                ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
                ('nppdvjthqldpwncqszvftbrmjlhg', 23),
                ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
                ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
]

def test(test_input, f):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = f(puzzle_input, True)
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print('input:', puzzle_input,
              '\nsolution:', solution,
              'expected:', expected,
              ('failed') if solution != expected else '')

test(TEST_INPUT_1, main_1)
solve = main_1("inputs/06-Tuning-Trouble.txt")
print("solution:", solve)

test(TEST_INPUT_2, main_2)
solve = main_2("inputs/06-Tuning-Trouble.txt")
print("solution:", solve)
