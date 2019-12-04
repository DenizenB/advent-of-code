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
    points = {}
    total_steps = 0
    point = (0,0)

    for direction in wire_path:
        delta = get_delta(direction[0])
        steps = int(direction[1:])

        for _ in range(steps):
            total_steps += 1
            point = tuple(map(sum, zip(point, delta)))

            if point not in points:
                points[point] = total_steps

    return points

def wire_distance(point, maps):
    distance = 0

    for m in maps:
        distance += m[point]

    return distance

def main():
    with open("3.txt") as f:
        wires = f.readlines()

    maps = []
    for wire in wires:
        wire_path = wire.rstrip("\n").split(",")
        maps.append(build_points(wire_path))

    intersections = set.intersection(*map(lambda d: set(d.keys()), maps))
    distances = {}

    for point in intersections:
        distances[point] = wire_distance(point, maps)

    nearest_intersection = min(distances, key=distances.get)
    print("Nearest intersection: {}".format(nearest_intersection))
    print("Wire distance: {}".format(distances.get(nearest_intersection)))

main()