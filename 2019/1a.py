with open("1.txt") as f:
    masses = map(int, f.readlines())

def calc_fuel(mass):
    return mass // 3 - 2

fuel = sum(map(calc_fuel, masses))
print("Fuel: {}".format(fuel))