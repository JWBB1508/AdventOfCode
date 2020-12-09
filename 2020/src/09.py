"""
https://adventofcode.com/2020/day/9
"""

import sys
import itertools


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [int(line.strip()) for line in file.readlines()]


def part_one(data, preamble_length):
    previous_numbers = []
    for i in range(preamble_length):
        previous_numbers.append(data[i])
    for i in range(preamble_length, len(data)):
        previous_number_combinations = itertools.combinations(previous_numbers, 2)
        combination_exists = False
        for combination in previous_number_combinations:
            if sum(combination) == data[i]:
                combination_exists = True
        if not (combination_exists):
            return data[i]
        del previous_numbers[0]
        previous_numbers.append(data[i])
    raise Exception("No value found that is not the sum of two preceding numbers")


def part_two(data):
    target = part_one(data, 25)
    for i in range(len(data)):
        increment = 0
        values = []
        while sum(values) < target:
            values.append(data[i + increment])
            increment += 1
        if sum(values) == target:
            return min(values) + max(values)
    raise Exception(f"No contiguous range found summing target value: {target}")


if __name__ == "__main__":
    data = get_data("09.txt")
    print(f"Part 1: {part_one(data, 25)}")
    print(f"Part 2: {part_two(data)}")