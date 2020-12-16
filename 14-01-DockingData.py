"""
The initialization program (your puzzle input) can either
update the bitmask or write a value to memory.

Values and memory addresses are both 36-bit unsigned integers.
For example, ignoring bitmasks for a moment, a line like
  mem[8] = 11
would write the value 11 to memory address 8.

bitmask is string of 36 bits
memory is initialized as zeros

The current bitmask is applied to values immediately before they are written to memory:
a 0 or 1 overwrites the corresponding bit in the value,
while an X leaves the bit in the value unchanged.

Goal: sum of all values left in memory
"""


def parse_file(input):
    """Yields an instruction_set
    {'mask': value, 'instuctions': [(memory_addr, value), (memory_addr, value)...]}."""
    with open(input) as file:
        instruction_set = {}
        for i, line in enumerate(file):
            if line.startswith('mask'):
                if i != 0:
                    yield instruction_set
                instruction_set['mask'] = line.split('mask = ')[1].strip()
                instruction_set['instructions'] = []
            else:
                memory_addr = int(line[4:line.find(']')])
                value = int(line.split(' = ')[1])
                instruction_set['instructions'].append((memory_addr, value))
        yield instruction_set


class DockingProgram():
    def __init__(self):
        self.memory = [0 for n in range(65437)]
        self.mask = ''
        self.mask_length = 0

    def get_memory(self):
        return self.memory

    def set_memory(self, address, value):
        result = value
        for i, addr in enumerate(self.mask):
            if addr == 'X':
                continue
            mask_bit = 2**(self.mask_length - i)  # iterate from left to right, so subtract i from total
            if value & mask_bit == 0 and addr == '1':
                result += mask_bit
            elif value & mask_bit != 0 and addr == '0':
                result -= mask_bit
        self.memory[address] = result

    def run_instructions(self, instruction_set):
        self.mask = instruction_set['mask']
        self.mask_length = len(self.mask) - 1
        for (memory_addr, value) in instruction_set['instructions']:
            self.set_memory(memory_addr, value)


def main(puzzle_input):
    program = DockingProgram()
    for instruction_set in puzzle_input:
        program.run_instructions(instruction_set)
    return sum(program.get_memory())


TEST_INPUT = [
    ("14-01-test-input.txt", 165),
]


def test(test_input):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = main(parse_file(puzzle_input))
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print(puzzle_input,
              'solution:', solution,
              'expected:', expected,
              ('failed', expected - solution) if solution != expected else '')


test(TEST_INPUT)


output = main(parse_file("14-01-input.txt"))
print("solution:", output)
