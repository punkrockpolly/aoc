"""
The boot code is represented as a text file with one instruction per line of text.
Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument.
For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0.
After an acc instruction, the instruction immediately below it is executed next.

jmp jumps to a new instruction relative to itself.
The next instruction to execute is found using the argument as an offset from the jmp instruction;
for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.

nop stands for No OPeration - it does nothing.
The instruction immediately below it is executed next.
"""


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line


def interpret_opcode(opcode):
    operation, argument = opcode.split()
    return (operation, argument)


def operate(value):
    if value[0] == '-':
        return 0 - int(value[1:])
    if value[0] == '+':
        return int(value[1:])
    else:
        raise Exception("Not a valid command")


def main(puzzle_input):
    """Immediately before any instruction is executed a second time, what value is in the accumulator?"""
    accumulator = 0
    line = 0
    seen_lines = []
    while True:
        if line in seen_lines:
            return accumulator
        seen_lines.append(line)
        operation, argument = interpret_opcode(puzzle_input[line])
        if operation == 'acc':
            accumulator += operate(argument)
            line += 1
        elif operation == 'jmp':
            line += operate(argument)
        elif operation == 'nop':
            line += 1


def test(test_input, expected):
        output = main(test_input)
        # print(pp, is_valid, expected_valid)
        assert output == expected


test_program = list(parse_file("08-01-test-input.txt"))
test(test_program, 5)

program = list(parse_file("08-01-input.txt"))
accumulator = main(program)
print("solution:", accumulator)
