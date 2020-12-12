from puzzle import BasePuzzle
import numpy as np


class Ship:
    movement_directions = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }

    rotation_directions = {
        'L': -1,
        'R': 1,
    }

    def __init__(self):
        self.position = (0,0)
        self.direction = 90

    def direction_vector(self):
        directions = list(self.movement_directions.values())
        index = self.direction // 90

        return directions[index]

    def move(self, instruction):
        direction = instruction[0]
        amount = int(instruction[1:])

        if direction == 'F':
            movement = np.multiply(self.direction_vector(), amount)
            self.position = np.add(self.position, movement)
        elif direction in self.movement_directions:
            movement = np.multiply(self.movement_directions[direction], amount)
            self.position = np.add(self.position, movement)
        elif direction in self.rotation_directions:
            rotation = self.rotation_directions[direction] * amount
            self.direction = (self.direction + rotation) % 360

    def manhattan_distance(self):
        x, y = self.position
        return abs(x) + abs(y)


class Puzzle(BasePuzzle):
    def solve(self):
        ship = Ship()

        for instruction in self.lines:
            ship.move(instruction)

        print(f"Manhattan distance: {ship.manhattan_distance()}")


if __name__ == "__main__":
    Puzzle().solve()
