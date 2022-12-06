"""
https://adventofcode.com/2022/day/6
"""

import sys


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines[0]


def part_one():
    input = get_data("06.txt")
    sequence_length = 4
    for i in range(sequence_length, len(input) + 1):
        if len(set(input[i - sequence_length : i])) == sequence_length:
            return i
    return input


def part_two():
    input = get_data("06.txt")
    sequence_length = 14
    for i in range(sequence_length, len(input) + 1):
        if len(set(input[i - sequence_length : i])) == sequence_length:
            return i
    return input


if __name__ == "__main__":
    print(part_one())
    print(part_two())
