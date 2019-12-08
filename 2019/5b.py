class Computer:
    def __init__(self, memory):
        self.pc = 0
        self.memory = memory
    
    def execute(self):
        while self.step():
            pass
        return self.memory[0]
    
    def step(self):
        op = self.memory[self.pc]

        if op > 99:
            # Drop opcode, order modes left-to-right, append zeros in case they were ommitted
            modes = str(op)[:-2][::-1] + "00"
            op %= 100
        else:
            modes = "00"

        if op == 99:
            # Exit
            return False
        elif op == 1:
            # Add
            self.put(3, self.get(1, modes[0]) + self.get(2, modes[1]))
            self.pc += 4
        elif op == 2:
            # Multiply
            self.put(3, self.get(1, modes[0]) * self.get(2, modes[1]))
            self.pc += 4
        elif op == 3:
            # Input
            input_value = int(input("> "))
            self.put(1, input_value)
            self.pc += 2
        elif op == 4:
            # Output
            print(self.get(1, modes[0]))
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
        self.put(3, output)
        self.pc += 4

    def get(self, offset, mode):
        if mode == "0":
            pointer = self.memory[self.pc + offset]
        elif mode == "1":
            pointer = self.pc + offset
        return self.memory[pointer]

    def put(self, offset, value):
        pointer = self.memory[self.pc + offset]
        self.memory[pointer] = value

def main():
    with open("5.txt") as f:
        memory = f.read().split(",")

    memory = list(map(int, memory))
    Computer(memory).execute()

main()