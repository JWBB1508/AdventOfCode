"""
https://adventofcode.com/2020/day/20
"""

import sys
import re


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]


def part_one(data):
    pass


def part_two(data):
    pass


if __name__ == "__main__":
    data = get_data("19.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
