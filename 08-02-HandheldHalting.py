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
    """The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file"""
    accumulator = 0
    line = 0
    seen_lines = []
    while True:
        if line == len(puzzle_input):
            return accumulator
        if line in seen_lines:  # still stuck in infinite loop
            return None
        seen_lines.append(line)
        operation, argument = interpret_opcode(puzzle_input[line])
        if operation == 'acc':
            accumulator += operate(argument)
            line += 1
        elif operation == 'jmp':
            line += operate(argument)
        elif operation == 'nop':
            line += 1


def change_line(puzzle_input):
    """Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp."""
    altered_input = puzzle_input.copy()
    other_op = {'jmp': 'nop', 'nop': 'jmp'}
    for n, line in enumerate(puzzle_input):
        op, argument = interpret_opcode(line)
        if op != 'acc':
            altered_input[n] = altered_input[n].replace(op, other_op[op])
            result = main(altered_input)
            if result:
                return result
            else:  # reset puzzle instructions and move on to trying the next line
                altered_input = puzzle_input.copy()


def test(test_input, expected):
        output = change_line(test_input)
        print(test_input, "output", output, "expected", expected)
        assert output == expected


test_program = list(parse_file("08-01-test-input.txt"))
test(test_program, 8)

program = list(parse_file("08-01-input.txt"))
accumulator = change_line(program)
print("solution:", accumulator)
