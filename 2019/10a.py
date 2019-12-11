class AsteroidMap:
    def __init__(self, map_str):
        self.asteroids = []

        lines = map_str.split('\n')
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                if line[x] == '#':
                    self.asteroids.append((x,y))

    def free_sight(self, a1, a2):
        x1, y1 = a1
        x2, y2 = a2

        # Define bounding box
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        # Solve for line equation, y = kx+m
        k = 0 if x1 == x2 else (y2 - y1) / (x2 - x1)
        m = y1 - k * x1

        can_see = True
        for a in self.asteroids:
            x, y = a

            if a == a1 or a == a2:
                continue

            if x < min_x or x > max_x or y < min_y or y > max_y:
                # Outside of bounding box; i.e. not between the asteroids
                continue

            if y == k * x + m:
                # Asteroid is in line of sight
                can_see = False
                break

        return can_see

    def count_visible(self, origin):
        visible = 0
        for a in self.asteroids:
            if a != origin and self.free_sight(origin, a):
                print("{} can see {}".format(origin, a))
                visible += 1
        print("{} can see {} asteroids".format(origin, visible))
        return visible

    def find_best(self):
        return max(self.asteroids, key=self.count_visible)

def main():
    with open("10.txt") as f:
        map_str = f.read()

    map_str = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""
    asteroid_map = AsteroidMap(map_str)
    best_asteroid = asteroid_map.find_best()
    visible_count = asteroid_map.count_visible(best_asteroid)
    print("Best asteroid is {} with free LoS to {} other asteroids".format(best_asteroid, visible_count))

main()