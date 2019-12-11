import math
from numpy import add, subtract, divide, multiply

class AsteroidMap:
    def __init__(self, map_str):
        self.asteroids = []

        lines = map_str.split('\n')
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                if line[x] == '#':
                    self.asteroids.append((x,y))

        self.max_x = max(map(lambda point: point[0], self.asteroids))
        self.max_y = max(map(lambda point: point[1], self.asteroids))

    def count_visible(self, origin):
        visible = self.asteroids.copy()

        for target in self.asteroids:
            if target == origin:
                visible.remove(target)
                continue

            diff = subtract(target, origin)
            step = divide(diff, math.gcd(*diff))

            for i in range(1, 2**31):
                hidden_point = tuple(add(target, multiply(step, i)))
                if hidden_point in visible:
                    visible.remove(hidden_point)

                x, y = hidden_point
                if x < 0 or y < 0 or x > self.max_x or y > self.max_y:
                    break

        return len(visible)

    def find_best(self):
        visible_counts = list(map(self.count_visible, self.asteroids))
        best_count = max(visible_counts)
        best_index = visible_counts.index(best_count)

        return (self.asteroids[best_index], best_count)

def main():
    with open("10.txt") as f:
        map_str = f.read()

    asteroid_map = AsteroidMap(map_str)
    asteroid, count = asteroid_map.find_best()
    print("Best asteroid is {} with free LoS to {} other asteroids".format(asteroid, count))

main()