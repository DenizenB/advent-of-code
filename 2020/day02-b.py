from puzzle import BasePuzzle

class Password:
    def __init__(self, line):
        rule, self.password = line.split(": ")
        positions, self.target_char = rule.split(" ")
        self.positions = [int(position) for position in positions.split("-")]

    def valid(self):
        x, y = self.positions

        return (self.password[x-1] == self.target_char) != (self.password[y-1] == self.target_char) # boolean xor

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