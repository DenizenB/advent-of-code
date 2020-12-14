from puzzle import BasePuzzle
from re import compile


class Decoder:
    memory_expr = compile("mem\[(\d+)\] = (\d+)")

    def __init__(self):
        self.memory = {}

    def set_mask(self, mask_str):
        self.mask_ones = int(mask_str.replace('X', '0'), base=2)
        self.mask_zeroes = int(mask_str.replace('X', '1'), base=2)

    def mask(self, value):
        value |= self.mask_ones
        value &= self.mask_zeroes
        return value

    def set_memory(self, address, value):
        value = self.mask(value)
        self.memory[address] = value

    def execute(self, line):
        if "mask" == line[0:4]:
            self.set_mask(line[7:])
        else:
            groups = self.memory_expr.fullmatch(line).groups()
            index, value = map(int, groups)

            self.set_memory(index, value)

    def memory_sum(self):
        return sum(self.memory.values())


class Puzzle(BasePuzzle):
    def solve(self, decoder):
        for line in self.lines:
            decoder.execute(line)

        print(f"Memory sum: {decoder.memory_sum()}")


if __name__ == "__main__":
    Puzzle().solve(Decoder())
