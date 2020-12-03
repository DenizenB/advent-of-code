from puzzle import BasePuzzle
import numpy as np

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
    def find_trees(self, slope):
        walker = Walker(self.lines, *slope)
        walker.walk()
        return walker.trees

    def solve(self):
        slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
        tree_counts = [self.find_trees(slope) for slope in slopes]
        tree_product = np.prod(tree_counts)

        print(f"Product: {tree_product}")

if __name__ == "__main__":
    Puzzle().solve()