from puzzle import BasePuzzle
from day05_a import Seat

class Puzzle(BasePuzzle):
    def solve(self):
        seats = map(Seat, self.lines)
        seats = sorted(seats, key = lambda s: s.id)

        for i in range(len(seats)):
            next_id = seats[i].id + 1
            next_seat = seats[i+1]

            if next_seat.id != next_id:
                print(f"Your seat: {next_id}")
                break

if __name__ == "__main__":
    Puzzle().solve()