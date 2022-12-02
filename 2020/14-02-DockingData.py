"""
The initialization program (your puzzle input) can either
update the bitmask or write a value to memory.

Values and memory addresses are both 36-bit unsigned integers.
For example, ignoring bitmasks for a moment, a line like
  mem[8] = 11
would write the value 11 to memory address 8.

bitmask is string of 36 bits
memory is initialized as zeros

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.

Goal: sum of all values left in memory
"""

from itertools import product


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

    def apply_mask(self, address):
        addr_bits = [n for n in '{0:036b}'.format(address)]
        mask_bits = [n for n in self.mask]
        masked_addr = []

        for addr, mask_bit in zip(addr_bits, mask_bits):
            if mask_bit == '0':
                masked_addr.append(addr)
            else:
                masked_addr.append(mask_bit)
        return masked_addr

    def replace_floating_bits(self, masked_addr, results):
        print(masked_addr, results)
        if masked_addr.count('X') == 0:
            return results
        else:
            x = masked_addr.index('X')
            addr_copy_1 = masked_addr.copy()
            addr_copy_0 = masked_addr.copy()
            addr_copy_1[x] = '1'
            addr_copy_0[x] = '0'
            results.append(self.replace_floating_bits(addr_copy_1, results))
            results.append(self.replace_floating_bits(addr_copy_0, results))

    def handle_floating_bits(self, value, floating_bits):
        bit_combinations = product(range(2), repeat=len(floating_bits))
        result_combinations = set()

        for combination in bit_combinations:
            for addr, bit in zip(combination, floating_bits):
                print(addr, bit, (value & bit) != 0)
                if value & bit == 0:
                    result_combinations.add(value + bit)
                    print("add value", bin(value + bit), value + bit)
                elif value & bit != 0 and addr == 0:
                    result_combinations.add(value - bit)
                    print("sub value", bin(value - bit), value - bit)
                else:
                    result_combinations.add(value)
                    print("same value", bin(value), value)
            # print('result_combinations', result_combinations)
        return result_combinations

    def set_memory(self, address, value):
        print(self.mask)
        masked_addr = self.apply_mask(address)
        results = self.replace_floating_bits(masked_addr, [])
        # for i, addr in enumerate(self.mask):
        #     if addr == '0':
        #         continue
        #     mask_bit = 2**(self.mask_length - i)  # iterate from left to right, so subtract i from total
        #     print(address, value, i, addr, mask_bit, address & mask_bit)
        #     if address & mask_bit == 0 and addr == '1':
        #         result += mask_bit
        #     elif addr == 'X':
        #         floating_bits.append(mask_bit)
        # print("before floating bits", floating_bits, bin(result))

        # results = self.handle_floating_bits(result, floating_bits) if floating_bits else result
        for memory_addr in results:
            memory_addr = int(memory_addr, 2)
            self.memory[memory_addr] = value
            print('set memory_addr', memory_addr, value)

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
    ("14-02-test-input.txt", 208),
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


# output = main(parse_file("14-01-input.txt"))
# print("solution:", output)
