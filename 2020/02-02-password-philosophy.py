def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


def count_pw(input):
    filtered = filter(filter_pw, parse_file(input))
    return len(list(filtered))


def filter_pw(line):
    "6-8 s: svsssszslpsp"
    rule, letter, pw = line.split()
    a, b = (int(n) - 1 for n in rule.split('-'))
    letter = letter[0]
    return (pw[a] == letter) != (pw[b] == letter)


def test(tests):
    for (t, expected) in tests:
        print((t, expected), filter_pw(t))
        assert filter_pw(t) == expected
        

tests = [("1-3 a: abcde", True),
("1-3 b: cdefg", False),
("2-9 c: ccccccccc", False)]

test(tests)

count = count_pw("02-01-input.txt") 
print(count)