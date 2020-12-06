def parse_file(input):
    """A very ugly way to yield multiline strings without regex."""
    with open(input) as file:
        p = ''
        for line in file:
            p += line
            if line == "\n":
                yield p.replace('\n', '')
                p = ''
        yield p.replace('\n', '')


def main(input):
    return sum(count_group(group) for group in input)


def count_group(group):
    return len(''.join(set(group)))


def test(test_input, expected):
    for form, expected_count in zip(test_input, expected):
        count = count_group(form)
        print(form, count, expected_count)
        assert count == expected_count

print(list(parse_file("06-01-test-input.txt")))

test(parse_file("06-01-test-input.txt"), [3, 3, 3, 1, 1])

count = main(parse_file("06-01-input.txt"))
print("solution:", count)
