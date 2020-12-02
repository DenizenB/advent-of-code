from puzzle import BasePuzzle

class Password:
    def __init__(self, line):
        rule, self.password = line.split(": ")
        counts, self.target_char = rule.split(" ")
        self.min_count, self.max_count = [int(count) for count in counts.split("-")]

    def valid(self):
        target_count = self.password.count(self.target_char)
        return target_count >= self.min_count and target_count <= self.max_count

class Puzzle(BasePuzzle):
    def solve(self):
        valid_passwords = 0

        for line in self.lines:
            password = Password(line)

            if password.valid():
                valid_passwords += 1

        print(f"Valid passwords: {valid_passwords}")


if __name__ == "__main__":
    Puzzle().solve()