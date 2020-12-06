from puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def solve(self):
        groups = self.input.split("\n\n")
        total = 0

        for group in groups:
            answers = [set(answer) for answer in group.split("\n")]
            intersection = set.intersection(*answers)

            total += len(intersection)

        print(f"Intersecting yeses by group: {total}")


if __name__ == "__main__":
    Puzzle().solve()
