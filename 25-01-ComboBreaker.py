"""
The handshake used by the card and the door involves an operation that
transforms a subject number.
To transform a subject number, start with the value 1.

Then, a number of times called the loop size, perform the following steps:

Set the value to itself multiplied by the subject number.
Set the value to the remainder after dividing the value by 20201227.
"""


def find_loop(public_key):
    value = 1
    subject_number = 7
    loop = 0
    while value != public_key:
        value *= subject_number
        value %= 20201227
        loop += 1
    return loop


def transform(public_key, loop):
    value = 1
    for i in range(loop):
        value *= public_key
        value %= 20201227
    return value


def main(card_public_key, door_public_key):
    car_loop = find_loop(card_public_key)

    encryption_key = transform(door_public_key, car_loop)
    return encryption_key


TEST_CARD_PUBLIC_KEY = 5764801
TEST_DOOR_PUBLIC_KEY = 17807724
TEST_SOLUTION = 14897079
encryption_key = main(TEST_CARD_PUBLIC_KEY, TEST_DOOR_PUBLIC_KEY)
assert encryption_key == TEST_SOLUTION

CARD_PUBLIC_KEY = 14222596
DOOR_PUBLIC_KEY = 4057428
encryption_key = main(CARD_PUBLIC_KEY, DOOR_PUBLIC_KEY)
print("solution:", encryption_key)
