"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID) -- optional

Count the number of valid passports
"""


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


def count_valid(input):
    filtered = filter(filter_passport, input)
    return len(list(filtered))


def filter_passport(pp):
    """
    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929
    """
    req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    data = pp.split()
    fields = {field.split(":")[0] for field in data}
    return req_fields.issubset(fields)


def test(test_input, expected):
    for pp, expected_valid in zip(test_input, expected):
        is_valid = filter_passport(pp)
        # print(pp, expected_valid)
        assert is_valid == expected_valid


test(parse_file("04-01-test-input.txt"), [True, False, True, False])

count = count_valid(parse_file("04-01-input.txt"))
print(count)
