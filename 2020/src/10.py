"""
https://adventofcode.com/2020/day/10
"""

import sys


def get_joltages(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        joltages = [int(line.strip()) for line in file.readlines()]
    joltages.append(0)
    joltages.sort()
    joltages.append(joltages[-1] + 3)
    return joltages


def part_one(joltages):
    one_jolt_differences = 0
    three_jolt_differences = 0
    for i in range(len(joltages) - 1):
        if joltages[i + 1] - joltages[i] > 3:
            raise Exception(
                f"Incompatible joltages at index: {i} ({joltages[i]} and {joltages[i+1]})"
            )
        if joltages[i + 1] - joltages[i] == 1:
            one_jolt_differences += 1
        elif joltages[i + 1] - joltages[i] == 3:
            three_jolt_differences += 1
    return one_jolt_differences * three_jolt_differences


def part_two(joltages):
    # For each adapter, work out how many possible routes can come after it
    possible_routes = [0] * len(joltages)
    # Start with the final (built-in device) adapter, no possible routes!
    j = len(joltages)
    i = j - 1
    possible_routes[i] = 0  # For clarity
    # For each of the possible adapters before it (max three!) there is one possible route
    # Then work down with the same logic
    j -= 1
    while j > 0:
        i = j - 1
        while i >= 0 and j - i <= 3:
            if joltages[j] - joltages[i] <= 3:
                possible_routes[i] += max(possible_routes[j], 1)
            i -= 1
        j -= 1
    return possible_routes[0]


if __name__ == "__main__":
    joltages = get_joltages("10.txt")
    print(f"Part 1: {part_one(joltages)}")
    print(f"Part 2: {part_two(joltages)}")