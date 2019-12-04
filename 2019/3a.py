def get_delta(bearing):
    if bearing == "R":
        return (1,0)
    elif bearing == "U":
        return (0,1)
    elif bearing == "L":
        return (-1,0)
    elif bearing == "D":
        return (0,-1)

def build_points(wire_path):
    points = set()
    point = (0,0)

    for direction in wire_path:
        delta = get_delta(direction[0])
        steps = int(direction[1:])

        for _ in range(steps):
            point = tuple(map(sum, zip(point, delta)))
            points.add(point)

    return points

def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    with open("3.txt") as f:
        wires = f.readlines()

    maps = []
    for wire in wires:
        wire_path = wire.rstrip("\n").split(",")
        maps.append(build_points(wire_path))

    intersections = set.intersection(*maps)
    distances = {}

    for point in intersections:
        distances[point] = manhattan_distance((0,0), point)

    nearest_intersection = min(distances, key=distances.get)
    print("Nearest intersection: {}".format(nearest_intersection))
    print("Manhattan distance: {}".format(distances.get(nearest_intersection)))

main()