from puzzle import BasePuzzle


class Adapter:
    def __init__(self, output_rating):
        self.output_rating = output_rating
        self.min_input = output_rating - 3
        self.max_input = output_rating - 1

    def acceptable_input(self, adapter):
        return adapter.output_rating >= self.min_input and adapter.output_rating <= self.max_input


class Diffcounter:
    def count_diffs(self, adapters):
        diffs = {1: 0, 2: 0, 3: 0}

        for i in range(len(adapters) - 1):
            output_adapter = adapters[i]
            input_adapter = adapters[i+1]

            if not input_adapter.acceptable_input(output_adapter):
                raise RuntimeError("Incompatible adapters")

            joltage_diff = input_adapter.output_rating - output_adapter.output_rating
            diffs[joltage_diff] += 1

        return diffs


class Pathfinder:
    def __init__(self, adapters):
        self.adapters = adapters
        self.known_paths = {}

    def count_paths_from(self, index):
        # Base case: reached final adapter
        if index == len(self.adapters) - 1:
            return 1

        # Base case: paths from this adapter have already been counted
        if index in self.known_paths:
            return self.known_paths[index]

        adapter = self.adapters[index]
        valid_paths = 0

        for next_index in range(index + 1, len(self.adapters)):
            next_adapter = self.adapters[next_index]

            if next_adapter.acceptable_input(adapter):
                valid_paths += self.count_paths_from(next_index)
            else:
                break

        self.known_paths[index] = valid_paths
        return valid_paths


class Puzzle(BasePuzzle):
    def solve(self):
        sorted_adapters = [Adapter(rating) for rating in sorted(self.integers())]
        max_output_rating = sorted_adapters[-1].output_rating

        outlet_adapter = Adapter(0)
        device_adapter = Adapter(max_output_rating + 3)

        sorted_adapters.insert(0, outlet_adapter)
        sorted_adapters.append(device_adapter)

        # Part one
        diffcounter = Diffcounter()
        diffs = diffcounter.count_diffs(sorted_adapters)
        print(f"d1 * d3 = {diffs[1] * diffs[3]}")

        # Part two
        pathfinder = Pathfinder(sorted_adapters)
        paths = pathfinder.count_paths_from(0)
        print(f"Valid paths: {paths}")


if __name__ == "__main__":
    Puzzle().solve()
