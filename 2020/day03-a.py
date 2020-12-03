from puzzle import BasePuzzle

class Walker:
    def __init__(self, lines, dx, dy):
        self.height = len(lines)
        self.width = len(lines[0])
        self.lines = lines

        self.x = 0
        self.y = 0
        self.trees = 0

        self.dx = dx
        self.dy = dy

    def step(self):
        cell = self.lines[self.y][self.x]
        if cell == "#":
            self.trees += 1

        self.x = (self.x + self.dx) % self.width
        self.y += self.dy

    def walk(self):
        while self.y < self.height:
            self.step()

class Puzzle(BasePuzzle):
    def solve(self):
        walker = Walker(self.lines, 3, 1)
        walker.walk()

        print(f"Trees: {walker.trees}")

if __name__ == "__main__":
    Puzzle().solve()