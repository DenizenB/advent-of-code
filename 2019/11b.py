from enum import Enum
from numpy import add

class Computer:
    def __init__(self, memory, io_device):
        self.memory = memory + [0 for _ in range(1000)]
        self.io_device = io_device
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
            input_value = self.io_device.read()
            self.put(1, modes[0], input_value)
            self.pc += 2
        elif op == 4:
            # Output
            output_value = self.get(1, modes[0])
            self.io_device.write(output_value)
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

class InputOutputDevice:
    def read(self):
        raise NotImplementedError

    def write(self, output):
        raise NotImplementedError

class HullPaintingRobot(InputOutputDevice):
    def __init__(self, hull_width, hull_height):
        self.panels = [[0 for _ in range(hull_width)] for _ in range(hull_height)]
        self.painted_panels = set()
        self.position = (int(hull_width / 2), int(hull_height / 2))
        self.direction = Direction.UP
        self.should_paint = True

        # Start position is painted white
        x, y = self.position
        self.panels[y][x] = 1

    def read(self):
        x, y = self.position
        return self.panels[y][x]

    def write(self, output):
        if self.should_paint:
            x, y = self.position
            self.panels[y][x] = output
            self.painted_panels.add((x,y))
        else:
            if output == 0:
                self.direction = self.direction.left()
            elif output == 1:
                self.direction = self.direction.right()

            self.position = add(self.position, self.direction.step())

        self.should_paint = not self.should_paint

    def count_painted_panels(self):
        return len(self.painted_panels)

    def finish_painting(self):
        for row in self.panels:
            print(''.join(map(lambda c: '#' if c == 1 else '.', row)))

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def right(self):
        if self == Direction.LEFT:
            return Direction.UP
        return Direction(self.value + 1)

    def left(self):
        if self == Direction.UP:
            return Direction.LEFT
        return Direction(self.value - 1)

    def step(self):
        return {
            Direction.UP: (0, -1),
            Direction.RIGHT: (1, 0),
            Direction.DOWN: (0, 1),
            Direction.LEFT: (-1, 0)
        }[self]

def main():
    with open("11.txt") as f:
        memory_txt = f.read()

    memory = list(map(int, memory_txt.split(",")))
    robot = HullPaintingRobot(140, 40)
    computer = Computer(memory, robot)
    computer.execute()
    robot.finish_painting()

main()