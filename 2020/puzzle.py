import sys

class BasePuzzle:
    def __init__(self):
        self.input = sys.stdin.read().rstrip("\n")
        self.lines = self.input.splitlines()

    def integers(self):
        return list(map(int, self.lines))