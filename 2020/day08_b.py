from puzzle import BasePuzzle
import re
from day08_a import GameConsole


class GameConsoleFuzzer:
    def __init__(self, instructions):
        self.instructions = instructions

    def replace_one_instruction(self, from_op, to_op):
        for i, instruction in enumerate(self.instructions):
            if from_op in instruction:
                instructions = self.instructions.copy()
                instructions[i] = instruction.replace(from_op, to_op)

                console = GameConsole(instructions)
                console.run_until_loop()

                if console.pc == len(instructions):
                    print(f"Patched {from_op} at {i} to {to_op}")
                    print(f"Accumulator after patch: {console.accumulator}")
                    return


class Puzzle(BasePuzzle):
    def solve(self):
        fuzzer = GameConsoleFuzzer(self.lines)

        fuzzer.replace_one_instruction("nop", "jmp")
        fuzzer.replace_one_instruction("jmp", "nop")


if __name__ == "__main__":
    Puzzle().solve()
