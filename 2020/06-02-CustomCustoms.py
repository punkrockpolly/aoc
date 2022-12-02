def parse_file(input):
    """A very ugly way to yield multiline strings without regex."""
    with open(input) as file:
        p = ''
        for line in file:
            p += line
            if line == "\n":
                yield p
                p = ''
        yield p


def main(input):
    return sum(count_group(group) for group in input)


def count_group(group):
    sets = filter(None, [set(g) for g in group.splitlines()])
    return len(set.intersection(*sets))


def test(test_input, expected):
    for form, expected_count in zip(test_input, expected):
        count = count_group(form)
        print("form:", form, "count:", count, "expect", expected_count)
        assert count == expected_count

print(list(parse_file("06-01-test-input.txt")))

test(parse_file("06-01-test-input.txt"), [3, 0, 1, 1, 1])

count = main(parse_file("06-01-input.txt"))
print("solution:", count)
