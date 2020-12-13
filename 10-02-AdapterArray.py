"""
Output joltage (your puzzle input).
Any given adapter can take an input 1, 2, or 3 jolts lower than its rating
and still produce its rated output joltage.
built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter

Charging outlet has an effective rating of 0 jolts
If you use every adapter in your bag at once,
what is the distribution of joltage differences between the charging outlet,
the adapters, and your device?
"""


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield int(line)


def get_answer(jolts):
    return jolts[1] * jolts[3]


def count_jolts(data):
    adapters = list(data)
    adapters.sort()
    combos = []

    for i, adapter in enumerate(adapters):
        if i + 2 == len(adapters):
            # last adapter is not optional
            if adapters
            print(jolts)
            return sum(combos)



def test(test_input, expected):
    assert count_jolts(test_input) == expected

test(parse_file("10-01-test-input.txt"), 19208)


jolts = count_jolts(parse_file("10-01-input.txt"))
print("solution:", get_answer(jolts))
