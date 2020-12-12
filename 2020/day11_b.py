from puzzle import BasePuzzle
from day11_a import SeatGrid as _SeatGrid
from copy import deepcopy


class SeatGrid(_SeatGrid):
    def tick(self):
        current_seats = self.seats
        new_seats = deepcopy(current_seats)

        for x in range(self.width):
            for y in range(self.height):
                seat = current_seats[y][x]
                visible_seats = list(self.visible_seats(x, y))
                occupied_visible = visible_seats.count('#')

                if seat == 'L' and occupied_visible == 0:
                    new_seats[y][x] = '#'
                elif seat == '#' and occupied_visible >= 5:
                    new_seats[y][x] = 'L'

        return SeatGrid(new_seats)

    def visible_seats(self, center_x, center_y):
        for diff_x, diff_y in self.adjacent_diffs:
            x = center_x
            y = center_y

            while True:
                x += diff_x
                y += diff_y

                if not self.is_inside(x, y):
                    break

                seat = self.seats[y][x]

                if seat != '.':
                    yield seat
                    break


class Puzzle(BasePuzzle):
    def solve(self):
        grid = SeatGrid([list(line) for line in self.lines])

        while True:
            new_grid = grid.tick()

            if new_grid.seats == grid.seats:
                # No change
                print(f"Occupied seats: {grid.occupied_seats()}")
                break

            grid = new_grid


if __name__ == "__main__":
    Puzzle().solve()
