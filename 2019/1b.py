with open("1.txt") as f:
    masses = map(int, f.readlines())

def calc_fuel(mass):
    fuel = mass // 3 - 2

    if fuel <= 0:
        return 0
    
    return fuel + calc_fuel(fuel)

fuel = sum(map(calc_fuel, masses))
print("Fuel: {}".format(fuel))