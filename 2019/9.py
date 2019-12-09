class Computer:
    def __init__(self, memory):
        self.memory = memory
        self.pc = 0
        self.relative_base = 0

    def execute(self):
        while self.step():
            pass

    def step(self):
        op = self.memory[self.pc]

        if op > 99:
            # Drop opcode, order modes left-to-right, append zeros in case they were ommitted
            modes = str(op)[:-2][::-1] + "000"
            op %= 100
        else:
            modes = "000"

        if op == 99:
            # Exit
            return False
        elif op == 1:
            # Add
            self.put(3, modes[2], self.get(1, modes[0]) + self.get(2, modes[1]))
            self.pc += 4
        elif op == 2:
            # Multiply
            self.put(3, modes[2], self.get(1, modes[0]) * self.get(2, modes[1]))
            self.pc += 4
        elif op == 3:
            # Input
            input_value = int(input("> "))
            self.put(1, modes[0], input_value)
            self.pc += 2
        elif op == 4:
            # Output
            output_value = self.get(1, modes[0])
            print(output_value)
            self.pc += 2
        elif op == 5:
            # Jump if true
            self.conditional_jump(lambda v: v != 0, modes)
        elif op == 6:
            # Jump if false
            self.conditional_jump(lambda v: v == 0, modes)
        elif op == 7:
            # Less than
            self.compare(lambda x, y: x < y, modes)
        elif op == 8:
            # Equals
            self.compare(lambda x, y: x == y, modes)
        elif op == 9:
            # Set relative base
            self.relative_base += self.get(1, modes[0])
            self.pc += 2
        else:
            print("Unknown opcode: {}".format(op))
            return False

        return True

    def conditional_jump(self, predicate, modes):
        if predicate(self.get(1, modes[0])):
            self.pc = self.get(2, modes[1])
        else:
            self.pc += 3

    def compare(self, comparator, modes):
        if comparator(self.get(1, modes[0]), self.get(2, modes[1])):
            output = 1
        else:
            output = 0
        self.put(3, modes[2], output)
        self.pc += 4

    def pointer(self, value, mode):
        if mode == "0":
            # Position
            return self.memory[self.pc + value]
        elif mode == "1":
            # Immediate
            return self.pc + value
        elif mode == "2":
            # Relative base
            return self.relative_base + self.memory[self.pc + value]

    def get(self, offset, mode):
        pointer = self.pointer(offset, mode)
        return self.memory[pointer]

    def put(self, offset, mode, value):
        pointer = self.pointer(offset, mode)
        self.memory[pointer] = value

def main():
    with open("9.txt") as f:
        memory = f.read().split(",")

    memory = list(map(int, memory))
    # Extend memory by 1000 positions
    memory += [0 for _ in range(1000)]

    computer = Computer(memory)
    computer.execute()

main()