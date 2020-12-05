from puzzle import BasePuzzle

class Seat:
    def __init__(self, pattern):
        row_min = 0
        row_max = 127
        col_min = 0
        col_max = 7

        for c in pattern:
            if c == "F":
                row_max = row_min + (row_max - row_min) // 2
            elif c == "B":
                row_min = row_max - (row_max - row_min) // 2
            elif c == "L":
                col_max = col_min + (col_max - col_min) // 2
            elif c == "R":
                col_min = col_max - (col_max - col_min) // 2

        if row_min != row_max or col_min != col_max:
            raise RuntimeError("your math sucks: {}".format([row_min, row_max, col_min, col_max]))

        self.row = row_min
        self.col = col_min
        self.id = row_min * 8 + col_min

class Puzzle(BasePuzzle):
    def solve(self):
        seats = map(Seat, self.lines)
        max_id = max(seats, key = lambda s: s.id).id

        print(f"Max id: {max_id}")

if __name__ == "__main__":
    Puzzle().solve()