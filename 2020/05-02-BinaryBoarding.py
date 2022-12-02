def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


def binary_space_partition(data):
    return [int(line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'),
            2) for line in data]


def find_seat(seats):
    seats.sort()

    for i, j in enumerate(seats, seats[0]):
        if i != j:
            return i


seats = binary_space_partition(parse_file("05-01-input.txt"))
print("solution:", find_seat(seats))
