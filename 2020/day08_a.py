from puzzle import BasePuzzle
import re


class GameConsole:
    instruction_expr = re.compile("(\w+) ([+\-0-9]+)")

    def __init__(self, instructions):
        self.instructions = instructions
        self.pc = 0
        self.accumulator = 0
        self.visited_instructions = set()

    def acc(self, value):
        self.accumulator += value
        self.pc += 1

    def jmp(self, value):
        self.pc += value

    def nop(self, value):
        self.pc += 1

    def execute_instruction(self):
        instruction = self.instructions[self.pc]
        self.visited_instructions.add(self.pc)

        op, arg = self.instruction_expr.fullmatch(instruction).groups()
        arg = int(arg)

        if op == "acc":
            self.acc(arg)
        elif op == "jmp":
            self.jmp(arg)
        elif op == "nop":
            self.nop(arg)

    def run_until_loop(self):
        while self.pc < len(self.instructions):
            if self.pc in self.visited_instructions:
                return

            self.execute_instruction()


class Puzzle(BasePuzzle):
    def solve(self):
        console = GameConsole(self.lines)
        console.run_until_loop()

        print(f"Accumulator at loop: {console.accumulator}")


if __name__ == "__main__":
    Puzzle().solve()
