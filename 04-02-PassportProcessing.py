from functools import partial

"""
Validation Rules

cid (Country ID) - ignored, missing or not.

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


def valid_yr(value, min, max):
    return int(value) >= min and int(value) <= max


def valid_hgt(value):
    """
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    """
    if value[-2:] == "cm":
        n = int(value[:-2])
        return n >= 150 and n <= 193
    elif value[-2:] == "in":
        n = int(value[:-2])
        return n >= 59 and n <= 76
    return False


def valid_hcl(value):
    """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
    valid_char = "0123456789abcdef"
    for char in value[1:]:
        if char not in valid_char:
            return False
    return value[0] == "#"


def valid_ecl(value):
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_pid(value):
    """pid (Passport ID) - a nine-digit number, including leading zeroes."""
    return len(value) == 9


def filter_passport(data):
    """
    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929
    """
    req_fields_missing = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    validation_rules = {
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        "byr": partial(valid_yr, min=1920, max=2002),
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        "iyr": partial(valid_yr, min=2010, max=2020),
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        "eyr": partial(valid_yr, min=2020, max=2030),
        "hgt": valid_hgt,
        "hcl": valid_hcl,
        "ecl": valid_ecl,
        "pid": valid_pid,
        "cid": lambda v: True}

    valid = []
    for field in data.split():
        k = field.split(":")[0]
        v = field.split(":")[1]
        valid.append(validation_rules[k](v))
        req_fields_missing.discard(k)
    # print(valid, req_fields_missing)
    return all(valid) and not req_fields_missing


def test(test_input, expected):
    for pp, expected_valid in zip(test_input, expected):
        is_valid = filter_passport(pp)
        # print(pp, is_valid, expected_valid)
        assert is_valid == expected_valid


test(parse_file("04-02-test-input.txt"), [False, False, False, False, True, True, True, True])

count = count_valid(parse_file("04-01-input.txt"))
print("solution:", count)
