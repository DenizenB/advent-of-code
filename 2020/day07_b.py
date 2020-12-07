from puzzle import BasePuzzle
from day07_a import Bag, BagFinder as _BagFinder


class BagFinder(_BagFinder):
    def find_bag(self, bag_name):
        bag = next(bag for bag in self.bags if bag.name == bag_name)
        return bag

    def find_contents_of(self, bag_name):
        bag = self.find_bag(bag_name)
        contents = 0

        for child_name, count in bag.contents.items():
            contents += count * (1 + self.find_contents_of(child_name))

        return contents

class Puzzle(BasePuzzle):
    def solve(self):
        bags = list(map(Bag, self.lines))
        finder = BagFinder(bags)

        gold_contents = finder.find_contents_of("shiny gold")
        print("Bags within the shiny gold bag: {}".format(gold_contents))

if __name__ == "__main__":
    Puzzle().solve()
