class Body:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.neighbors = set()

    def set_parent(self, parent):
        self.parent = parent
        self.neighbors.add(parent)
        parent.neighbors.add(self)

class System:
    def __init__(self):
        self.bodies = {'COM': Body('COM')}

    def get_body(self, name):
        if name in self.bodies:
            return self.bodies[name]

        body = Body(name)
        self.bodies[name] = body
        return body

    def shortest_path(self, origin, destination):
        # Djikstra's algorithm
        queue = []
        distance = {}
        previous = {}

        for body in self.bodies.values():
            queue.append(body)
            distance[body] = 2**31
            previous[body] = None

        distance[origin] = 0

        while queue:
            current = min(queue, key=lambda body: distance[body])
            queue.remove(current)

            for neighbor in current.neighbors:
                new_distance = distance[current] + 1
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    previous[neighbor] = current

        return distance[destination]

def main():
    system = System()

    with open("6.txt") as f:
        orbits = map(lambda line: line.rstrip('\n').split(')'), f.readlines())

    for parent_name, child_name in orbits:
        parent = system.get_body(parent_name)
        child = system.get_body(child_name)

        child.set_parent(parent)

    your_orbit = system.get_body('YOU').parent
    santas_orbit = system.get_body('SAN').parent
    hops = system.shortest_path(your_orbit, santas_orbit)

    print("Getting to Santa requires {} orbital transfers".format(hops))
main()