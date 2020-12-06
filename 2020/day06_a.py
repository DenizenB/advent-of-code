from puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def solve(self):
        groups = self.input.split("\n\n")
        total = 0

        for group in groups:
            answers = group.replace("\n", "")
            answers = set(answers)

            total += len(answers)

        print(f"Unique yeses by group: {total}")


if __name__ == "__main__":
    Puzzle().solve()
