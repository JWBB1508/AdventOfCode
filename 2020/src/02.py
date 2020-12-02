"""
https://adventofcode.com/2020/day/2
"""

import sys
import regex as re


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [line.strip() for line in file.readlines()]


def part_one(data):
    valid_passwords = 0
    for line in data:
        regex = re.compile(r"(\d+)-(\d+)\s+(\w+)\s*:\s*(\w+)")
        match = regex.match(line)
        min_occurs = int(match.group(1))
        max_occurs = int(match.group(2))
        character = match.group(3)
        password = match.group(4)
        occurences = 0
        for pass_char in password:
            if pass_char == character:
                occurences += 1
        if occurences >= min_occurs and occurences <= max_occurs:
            valid_passwords += 1
    return valid_passwords


def part_two(data):
    valid_passwords = 0
    for line in data:
        regex = re.compile(r"(\d+)-(\d+)\s+(\w+)\s*:\s*(\w+)")
        match = regex.match(line)
        pos_1 = int(match.group(1))
        pos_2 = int(match.group(2))
        character = match.group(3)
        password = match.group(4)
        occurences = 0
        for i, pass_char in enumerate(password):
            if (i + 1 == pos_1 or i + 1 == pos_2) and pass_char == character:
                occurences += 1
        if occurences == 1:
            valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    data = get_data("02.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
