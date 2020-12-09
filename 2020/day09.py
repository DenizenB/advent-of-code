from puzzle import BasePuzzle


class XmasDecoder:
    def __init__(self, numbers, preamble_size):
        self.numbers = numbers
        self.preamble_size = preamble_size

    def valid_numbers_at(self, index):
        previous_numbers = self.numbers[index-self.preamble_size: index]

        for x in previous_numbers:
            for y in previous_numbers:
                yield x + y

    def find_invalid_number(self):
        for i in range(self.preamble_size, len(self.numbers)):
            number = self.numbers[i]

            if number not in self.valid_numbers_at(i):
                return number

        raise RuntimeError("No invalid number")

    def find_weakness(self, invalid_number):
        for start in range(len(self.numbers)):
            total = self.numbers[start]

            for end in range(start + 1, len(self.numbers)):
                total += self.numbers[end]

                if total == invalid_number:
                    number_range = self.numbers[start:end+1]
                    key = min(number_range) + max(number_range)
                    return key

        raise RuntimeError("No weakness")


class Puzzle(BasePuzzle):
    def solve(self):
        decoder = XmasDecoder(self.integers(), 25)

        invalid_number = decoder.find_invalid_number()
        print(f"Invalid number: {invalid_number}")

        weakness = decoder.find_weakness(invalid_number)
        print(f"Weakness: {weakness}")


if __name__ == "__main__":
    Puzzle().solve()
