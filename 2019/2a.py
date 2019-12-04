class Computer:
    def __init__(self, memory):
        self.pc = 0
        self.memory = memory
    
    def execute(self):
        while self.pc >= 0 and self.pc < len(self.memory):
            self.step()
        return self.memory[0]
    
    def step(self):
        op = self.memory[self.pc]

        if op is 99:
            self.pc = -1
        elif op is 1:
            self.put(3, self.get(1) + self.get(2))
            self.pc += 4
        elif op is 2:
            self.put(3, self.get(1) * self.get(2))
            self.pc += 4
        else:
            print("Unknown op: {}".format(op))
            self.pc = -1

    def get(self, offset):
        pointer = self.memory[self.pc + offset]
        return self.memory[pointer]
    
    def put(self, offset, value):
        pointer = self.memory[self.pc + offset]
        self.memory[pointer] = value

def main():
    with open("2.txt") as f:
        memory = f.read().split(",")

    memory = list(map(int, memory))
    memory[1] = 12
    memory[2] = 2

    output = Computer(memory).execute()

    print("Computation: {}".format(output))

main()