"""
https://adventofcode.com/2020/day/1
"""

import sys


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [int(line.strip()) for line in file.readlines()]


def part_one(data):
    for i in range(len(data)):
        if data[i] > 2020:
            continue
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]
    raise Exception("Entries with sum of 2020 not found")


def part_two(data):
    for i in range(len(data)):
        if data[i] > 2020:
            continue
        for j in range(i + 1, len(data)):
            if data[i] + data[j] > 2020:
                continue
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]
    raise Exception("Entries with sum of 2020 not found")


if __name__ == "__main__":
    data = get_data("01.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
