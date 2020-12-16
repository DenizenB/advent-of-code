from puzzle import BasePuzzle

class RecitationGame:
    def __init__(self, numbers):
        self.rounds_played = 0
        self.numbers = {}
        self.last_number = None

        for number in numbers:
            self.say(number)

    def say(self, number):
        if self.last_number != None:
            self.numbers[self.last_number] = self.rounds_played

        self.last_number = number
        self.rounds_played += 1

    def tick(self):
        next_number = 0

        if self.last_number in self.numbers:
            last_round = self.numbers[self.last_number]
            next_number = self.rounds_played - last_round

        self.say(next_number)

    def play_until_round(self, target_round):
        while self.rounds_played < target_round:
            self.tick()

        print(f"{target_round}th number: {self.last_number}")


class Puzzle(BasePuzzle):
    def solve(self):
        numbers = [int(value) for value in self.lines[0].split(',')]
        game = RecitationGame(numbers)

        # Part one
        game.play_until_round(2020)

        # Part two
        game.play_until_round(30000000)


if __name__ == "__main__":
    Puzzle().solve()
