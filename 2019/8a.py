def chunks(lst, size):
    for chunk_start in range(0, len(lst), size):
        yield lst[chunk_start:chunk_start + size]

class SpaceImageDecoder:
    def __init__(self, image_str, width, height):
        self.width = width
        self.height = height
        self.layers = []
        for chunk_str in chunks(image_str, width * height):
            self.layers.append(list(map(int, chunk_str)))

    def checksum(self):
        layer = min(self.layers, key=lambda layer: layer.count(0))
        return layer.count(1) * layer.count(2)

def main():
    with open("8.txt") as f:
        image_str = f.read().rstrip('\n')

    decoder = SpaceImageDecoder(image_str, 25, 6)
    print("Checksum: {}".format(decoder.checksum()))

main()