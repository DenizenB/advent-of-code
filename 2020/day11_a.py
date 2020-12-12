from puzzle import BasePuzzle
from copy import deepcopy


class SeatGrid:
    """
        Grid of seats.

        . = floor  
        L = available  
        # = occupied
    """

    adjacent_diffs = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1)
    ]

    def __init__(self, seats):
        self.seats = seats
        self.height = len(seats)
        self.width = len(seats[0])

    def tick(self):
        current_seats = self.seats
        new_seats = deepcopy(current_seats)

        for x in range(self.width):
            for y in range(self.height):
                seat = current_seats[y][x]
                adjacent_seats = list(self.adjacent_seats(x, y))
                occupied_adjacents = adjacent_seats.count('#')

                if seat == 'L' and occupied_adjacents == 0:
                    new_seats[y][x] = '#'
                elif seat == '#' and occupied_adjacents >= 4:
                    new_seats[y][x] = 'L'

        return SeatGrid(new_seats)

    def adjacent_seats(self, center_x, center_y):
        for diff_x, diff_y in self.adjacent_diffs:
            x = center_x + diff_x
            y = center_y + diff_y

            if not self.is_inside(x, y):
                continue

            seat = self.seats[y][x]

            if seat != '.':
                yield seat

    def is_inside(self, x, y):
        return (x >= 0 and x < self.width
            and y >= 0 and y < self.height)

    def occupied_seats(self):
        return sum(map(lambda line: line.count("#"), self.seats))


class Puzzle(BasePuzzle):
    def solve(self):
        grid = SeatGrid([list(line) for line in self.lines])

        # Part one

        while True:
            new_grid = grid.tick()

            if new_grid.seats == grid.seats:
                # No change
                print(f"Occupied seats: {grid.occupied_seats()}")
                break

            grid = new_grid


if __name__ == "__main__":
    Puzzle().solve()
