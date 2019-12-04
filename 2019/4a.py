def valid(password):
    has_adjacents = False
    decreasing = False

    previous = None

    for digit in str(password):
        if digit == previous:
            has_adjacents = True

        if previous is not None and digit < previous:
            decreasing = True
            break

        previous = digit

    return has_adjacents and not decreasing

def main():
    with open("4.txt") as f:
        bounds = f.read().split("-")
    
    bounds = tuple(map(int, bounds))
    matching = 0

    for password in range(bounds[0], bounds[1]+1):
        if valid(password):
            matching += 1

    print("Matching passwords: {}".format(matching))

main()