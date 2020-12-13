from puzzle import BasePuzzle
from sympy.ntheory.modular import crt


class Bus:
    def __init__(self, bus_id):
        self.id = bus_id

    def time_to_next_departure(self, time):
        return -time % self.id


class Timetable:
    def __init__(self, buses):
        self.buses = buses

    def departures_at(self, time):
        wait_times = map(lambda bus: bus.time_to_next_departure(time), self.buses)
        return zip(wait_times, self.buses)

    def next_departure(self, time):
        return min(self.departures_at(time))


class Puzzle(BasePuzzle):
    def solve(self):
        raw_timetable = self.lines[1].split(',')
        buses = [Bus(int(bus_id)) for bus_id in raw_timetable if bus_id != 'x']
        timetable = Timetable(buses)

        # Part one

        start_time = int(self.lines[0])
        wait_time, bus = timetable.next_departure(start_time)

        print(f"Earliest departure with bus {bus.id}, waiting for {wait_time} minutes")
        print(f"Answer: {bus.id * wait_time}")

        # Part two

        moduli = []
        remainders = []

        for offset, bus_id in enumerate(raw_timetable):
            if bus_id == 'x':
                continue

            bus_id = int(bus_id)

            moduli.append(bus_id)
            remainders.append(-offset % bus_id)

        earliest_time, _ = crt(moduli, remainders)
        print(f"The time you're looking for is {earliest_time}")


if __name__ == "__main__":
    Puzzle().solve()
