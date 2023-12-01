"""
https://adventofcode.com/2022/day/7
"""

import sys


class Directory:
    def __init__(self, name: str, child_dirs: list[str], child_file_size: int):
        self.name = name
        self.child_dirs = child_dirs
        self.child_file_size = child_file_size


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    i = 0
    directories = []
    while i < len(lines):
        if "$ ls" not in lines[i]:
            i += 1
            continue
        child_dirs = []
        child_file_size = 0
        j = 1
        while i + j < len(lines):
            if "$" in lines[i + j]:
                break


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
