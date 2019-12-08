class Body:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def count_orbits(self):
        orbits = 0
        parent = self.parent

        while parent is not None:
            orbits += 1
            parent = parent.parent

        return orbits

class System:
    def __init__(self):
        self.bodies = {'COM': Body('COM')}

    def get_body(self, name):
        if name in self.bodies:
            return self.bodies[name]

        body = Body(name)
        self.bodies[name] = body
        return body

    def count_total_orbits(self):
        return sum(map(lambda body: body.count_orbits(), self.bodies.values()))

def main():
    system = System()

    with open("6.txt") as f:
        orbits = map(lambda line: line.rstrip('\n').split(')'), f.readlines())

    for parent_name, child_name in orbits:
        parent = system.get_body(parent_name)
        child = system.get_body(child_name)

        child.parent = parent

    print("Total orbits: {}".format(system.count_total_orbits()))

main()