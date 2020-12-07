from puzzle import BasePuzzle
import re


class Bag:
    name_expr = re.compile("(.*) bags contain")
    contents_expr = re.compile("(\d+) ([^\d]+) bag")

    def __init__(self, rule):
        self.name = self.name_expr.match(rule).groups()[0]

        self.contents = {}
        for count, name in self.contents_expr.findall(rule):
            self.contents[name] = int(count)

    def __str__(self):
        return self.name

class BagFinder:
    def __init__(self, bags):
        self.bags = bags

    def find_containers_of(self, bag_name):
        containers = filter(lambda bag: bag_name in bag.contents, self.bags)
        containers = set(map(lambda bag: bag.name, containers))

        for container in containers:
            containers = containers.union(self.find_containers_of(container))

        return containers

class Puzzle(BasePuzzle):
    def solve(self):
        bags = list(map(Bag, self.lines))
        finder = BagFinder(bags)

        containers = finder.find_containers_of("shiny gold")
        print("Containers: {}".format(len(containers)))

if __name__ == "__main__":
    Puzzle().solve()
