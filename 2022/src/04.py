"""
https://adventofcode.com/2022/day/4
"""

import sys


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [line.strip().split(",") for line in file.readlines()]


def get_min(range):
    return int(range.split("-")[0])


def get_max(range):
    return int(range.split("-")[1])


def part_one():
    pairs = get_data("04.txt")
    enclaved_pairs = 0
    for pair in pairs:
        if (
            get_min(pair[0]) >= get_min(pair[1])
            and get_min(pair[0]) <= get_max(pair[1])
            or get_min(pair[1]) >= get_min(pair[0])
            and get_min(pair[1]) <= get_max(pair[0])
            or get_max(pair[0]) <= get_max(pair[1])
            and get_max(pair[0]) >= get_min(pair[1])
            or get_max(pair[1]) <= get_max(pair[0])
            and get_max(pair[1]) >= get_min(pair[0])
        ):
            enclaved_pairs += 1
    return enclaved_pairs


if __name__ == "__main__":
    print(part_one())
