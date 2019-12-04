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

        if op is 99:
            return False
        elif op is 1:
            self.put(3, self.get(1) + self.get(2))
        elif op is 2:
            self.put(3, self.get(1) * self.get(2))

        self.pc += 4
        return True

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

    for noun in range(0, 100):
        for verb in range(0, 100):
            memory[1] = noun
            memory[2] = verb

            computer = Computer(memory.copy())
            output = computer.execute()

            if output == 19690720:
                print("Found match with noun {} and verb {}, resulting in {}".format(noun, verb, 100 * noun + verb))
                return

main()