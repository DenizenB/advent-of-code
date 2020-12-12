from puzzle import BasePuzzle
from day12_a import Ship as _Ship
import numpy as np


class Ship(_Ship):
    def __init__(self):
        super().__init__()
        self.waypoint = (10, 1)

    def direction_vector(self):
        return self.waypoint

    def rotate_waypoint(self, rotation):
        clockwise_rotations = (rotation % 360) // 90
        x, y = self.waypoint

        for i in range(clockwise_rotations):
            prev_x = x
            x = y
            y = -prev_x

        self.waypoint = (x, y)

    def move(self, instruction):
        direction = instruction[0]
        amount = int(instruction[1:])

        if direction == 'F':
            movement = np.multiply(self.direction_vector(), amount)
            self.position = np.add(self.position, movement)
        elif direction in self.movement_directions:
            movement = np.multiply(self.movement_directions[direction], amount)
            self.waypoint = np.add(self.waypoint, movement)
        elif direction in self.rotation_directions:
            rotation = self.rotation_directions[direction] * amount
            self.rotate_waypoint(rotation)


class Puzzle(BasePuzzle):
    def solve(self):
        ship = Ship()

        for instruction in self.lines:
            ship.move(instruction)

        print(f"Manhattan distance: {ship.manhattan_distance()}")


if __name__ == "__main__":
    Puzzle().solve()
