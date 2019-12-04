def valid(password):
    has_pair = False
    decreasing = False

    previous = None
    group_length = 1

    for digit in str(password):
        if digit == previous:
            group_length += 1
        else:
            if group_length == 2:
                has_pair = True
            group_length = 1

        if previous is not None and digit < previous:
            decreasing = True
            break

        previous = digit

    # Check if last group is a pair
    if group_length == 2:
        has_pair = True

    return has_pair and not decreasing

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