"""
https://adventofcode.com/2020/day/12
"""

import sys
from numpy import lcm, int64


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    earliest_time = int(lines[0])
    buses = [bus for bus in lines[1].split(",")]
    return earliest_time, buses


def part_one(data):
    init_time = data[0]
    time = init_time - 1
    correct_bus = None
    while not correct_bus:
        time += 1
        for bus in [int(bus) for bus in data[1] if bus != "x"]:
            if time % bus == 0:
                correct_bus = bus
    return correct_bus * (time - init_time)


def part_two(data):
    buses_by_offset = {}
    for i, bus in enumerate(data[1]):
        if bus != "x":
            buses_by_offset[i] = int(bus)
    time = -1
    solved = False
    step = 1
    buses_matched = set()
    while not solved:
        solved = True
        time += step
        num_buses_matched = 0
        for offset, bus in buses_by_offset.items():
            if (time + offset) % bus == 0:
                num_buses_matched += 1
                if num_buses_matched > len(buses_matched):
                    buses_matched.add(bus)
                    # Full disclosure: I saw a spoiler on Reddit about Chinese Remainder
                    # Theorem that pointed me in this general direction :(
                    step = lcm.reduce(list(buses_matched), dtype=int64)
                continue
            else:
                solved = False
                break
    return time


def part_two_brute_force(data):
    """Unsurprisingly, takes far too long to be useful"""
    start_time = -1
    solved = False
    while not solved:
        start_time += 1
        current_time = start_time - 1
        solved = True
        for bus in data[1]:
            current_time += 1
            if bus == "x":
                continue
            bus = int(bus)
            if current_time % bus == 0:
                continue
            else:
                solved = False
                break
    return start_time


if __name__ == "__main__":
    data = get_data("13.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")