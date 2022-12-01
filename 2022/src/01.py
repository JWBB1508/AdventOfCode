"""
https://adventofcode.com/2022/day/1
"""

import sys
from itertools import groupby


def get_data(filename):
    elves = []
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    i = 0
    food = []
    while i < len(lines):
        food.append(int(lines[i]))
        if i == len(lines) - 1 or lines[i + 1] == "":
            elves.append(food)
            food = []
            i += 1
        i += 1
    return elves


def part_one():
    elves = get_data("01.txt")
    max_calories = 0
    for elf in elves:
        calories = sum(elf)
        if calories > max_calories:
            max_calories = calories
    return max_calories


def part_two():
    elves = get_data("01.txt")
    elves.sort(key=lambda elf: sum(elf), reverse=True)
    return sum([sum(elf) for elf in elves[:3]])


if __name__ == "__main__":
    print(part_one())
    print(part_two())
