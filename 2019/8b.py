import sys

def chunks(lst, size):
    for chunk_start in range(0, len(lst), size):
        yield lst[chunk_start:chunk_start + size]

class SpaceImageDecoder:
    # Black => empty space, white => full block
    colors = colors = [' ', '\u2588']

    def __init__(self, image_str, width, height):
        self.width = width
        self.height = height
        self.layers = []
        for chunk_str in chunks(image_str, width * height):
            self.layers.append(list(map(int, chunk_str)))

    def checksum(self):
        layer = min(self.layers, key=lambda layer: layer.count(0))
        return layer.count(1) * layer.count(2)

    def decode(self):
        layer_size = self.width * self.height

        for i in range(layer_size):
            for layer in self.layers:
                if layer[i] != 2:
                    # First non-transparent color
                    sys.stdout.write(self.colors[layer[i]])
                    break

            if (i + 1) % self.width == 0:
                sys.stdout.write('\n')

def main():
    with open("8.txt") as f:
        image_str = f.read().rstrip('\n')

    decoder = SpaceImageDecoder(image_str, 25, 6)
    decoder.decode()

main()