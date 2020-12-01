from puzzle import BasePuzzle

class Puzzle(BasePuzzle):
    def solve(self):
        numbers = self.integers()

        for x in numbers:
            for y in numbers:
                total = x+y

                if total == 2020:
                    product = x*y

                    print(product)
                    return

if __name__ == "__main__":
    Puzzle().solve()