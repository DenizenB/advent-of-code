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

    def angle(self, origin, target):
        # Angle 0 straight up, clockwise rotation
        angle = math.atan2(target[0] - origin[0], origin[1] - target[1])
        return angle if angle >= 0 else angle + 2 * math.pi

    def dist_sq(self, origin, target):
        return (target[0] - origin[0])**2 + (target[1] - origin[1])**2

    def deploy_laser(self, origin):
        asteroid_angles = {}

        # Loop through asteroids, ordered by distance from origin
        for target in sorted(self.asteroids, key=lambda target: self.dist_sq(origin, target)):
            if target == origin:
                continue

            angle = self.angle(origin, target)
            if angle in asteroid_angles:
                asteroid_angles[angle].append(target)
            else:
                asteroid_angles[angle] = [target]

        angles = sorted(asteroid_angles)

        explosions = 0
        while angles:
            for angle in angles.copy():
                asteroids = asteroid_angles[angle]
                target = asteroids.pop(0)

                explosions += 1

                # Return 200th asteroid
                if explosions == 200:
                    return target

                # Last asteroid at this angle?
                if not asteroids:
                    angles.remove(angle)

def main():
    with open("10.txt") as f:
        map_str = f.read()

    asteroid_map = AsteroidMap(map_str)

    origin = (14, 17) # From 10a
    winner = asteroid_map.deploy_laser(origin)
    print("The 200th vaporized asteroid is {}".format(winner))

main()