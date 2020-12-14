from day14_a import Puzzle, Decoder
from itertools import product


class DecoderV2(Decoder):
    def set_mask(self, mask_str):
        # 0s are ignored
        self.mask_ones = int(mask_str.replace('X', '0'), base=2)
        self.floating_indexes = [i for (i, val) in enumerate(mask_str) if val == 'X']

    def mask(self, address):
        address |= self.mask_ones
        address_str = "{0:>036b}".format(address)

        floating_permutations = product(["0", "1"], repeat=len(self.floating_indexes))

        for bits in floating_permutations:
            new_address = list(address_str)

            for index, bit in zip(self.floating_indexes, bits):
                new_address[index] = bit

            new_address = int("".join(new_address), base=2)
            yield new_address

    def set_memory(self, address, value):
        for address in self.mask(address):
            self.memory[address] = value


if __name__ == "__main__":
    Puzzle().solve(DecoderV2())
