"""
https://adventofcode.com/2022/day/3
"""

import sys


def get_data(filename):
    backpacks = []
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            backpacks.append([line[: len(line) // 2], line[len(line) // 2 :]])
    return backpacks


def get_common_item(compartment_one, compartment_two):
    return set(compartment_one).intersection(set(compartment_two)).pop()


def get_badge(backpack_one, backpack_two, backpack_three):
    return (
        set(backpack_one)
        .intersection(set(backpack_two))
        .intersection(set(backpack_three))
        .pop()
    )


def get_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def part_one():
    backpacks = get_data("03.txt")
    common_items = []
    for backpack in backpacks:
        common_items.append(get_common_item(backpack[0], backpack[1]))
    return sum([get_priority(item) for item in common_items])


def part_two():
    backpacks = [backpack[0] + backpack[1] for backpack in get_data("03.txt")]
    badges = []
    for i in range(0, len(backpacks) - 2, 3):
        badges.append(get_badge(backpacks[i], backpacks[i + 1], backpacks[i + 2]))
    return sum([get_priority(badge) for badge in badges])


if __name__ == "__main__":
    print(part_one())
    print(part_two())
