"""
https://adventofcode.com/2020/day/15
"""

import sys
from tqdm import tqdm


def get_starting_numbers(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [int(value) for value in file.readlines()[0].strip().split(",")]


def part_one(starting_numbers):
    turn_last_spoken_by_number = {}
    last_number_spoken = None
    for i, number in enumerate(starting_numbers):
        last_number_spoken = number
        turn_last_spoken_by_number[number] = i
    for i in range(len(starting_numbers), 2020):
        if last_number_spoken in turn_last_spoken_by_number.keys():
            number = i - 1 - turn_last_spoken_by_number[last_number_spoken]
        else:
            number = 0
        turn_last_spoken_by_number[last_number_spoken] = i - 1
        last_number_spoken = number
    return last_number_spoken


def part_two(starting_numbers):
    """Same method as Part 1 ~ 14 seconds"""
    turn_last_spoken_by_number = {}
    last_number_spoken = None
    for i, number in enumerate(starting_numbers):
        last_number_spoken = number
        turn_last_spoken_by_number[number] = i
    for i in tqdm(range(len(starting_numbers), 30000000)):
        if last_number_spoken in turn_last_spoken_by_number.keys():
            number = i - 1 - turn_last_spoken_by_number[last_number_spoken]
        else:
            number = 0
        turn_last_spoken_by_number[last_number_spoken] = i - 1
        last_number_spoken = number
    return last_number_spoken


if __name__ == "__main__":
    starting_numbers = get_starting_numbers("15.txt")
    print(f"Part 1: {part_one(starting_numbers)}")
    print(f"Part 2: {part_two(starting_numbers)}")