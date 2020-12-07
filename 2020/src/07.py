"""
https://adventofcode.com/2020/day/7
"""

import sys
import re


class BagRules:
    def __init__(self, colour, inner_bag_count_by_colour):
        self.colour = colour
        self.inner_bag_count_by_colour = inner_bag_count_by_colour

    def __str__(self):
        return f"{self.colour} bags contain {', '.join([f'{num} {colour} bags' for colour, num in self.inner_bag_count_by_colour.items()]) if self.inner_bag_count_by_colour else 'no other bags'}."


def get_bag_rules(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    regex = re.compile(r"^(.*?) bags contain (.*).$")
    inner_regex = re.compile(r"^(\d+) (.*) bags?$")
    bag_rules = {}
    for line in lines:
        match = regex.search(line)
        if not match:
            raise Exception(f"Regex match failed on line: {line}")
        colour = match.group(1)
        inner_bags = match.group(2).split(", ")
        inner_bag_count_by_colour = {}
        for inner_bag in inner_bags:
            inner_match = inner_regex.search(inner_bag)
            if not inner_match:
                if inner_bag == "no other bags":
                    continue
                raise Exception(f"Regex match failed on line: {inner_bag}")
            inner_bag_count_by_colour[inner_match.group(2)] = int(inner_match.group(1))
        bag_rules[colour] = BagRules(colour, inner_bag_count_by_colour)
    return bag_rules


def part_one(bag_rules):
    """
    How many bags can contain, at any level, a shiny gold bag?
    The shiny gold bag must be contained by at least one other bag.
    """
    bag_count = 0
    for colour in bag_rules.keys():
        if bag_contains_colour(colour, "shiny gold", bag_rules):
            bag_count += 1
    return bag_count


def part_two(bag_rules):
    """
    How many bags must a single shiny gold bag contain?
    """
    count = [0]
    get_bag_count("shiny gold", bag_rules, count)
    return count[0]


def bag_contains_colour(container_colour, inner_colour, bag_rules):
    if inner_colour in bag_rules[container_colour].inner_bag_count_by_colour.keys():
        return True
    for inner_bag_colour in bag_rules[
        container_colour
    ].inner_bag_count_by_colour.keys():
        if bag_contains_colour(inner_bag_colour, inner_colour, bag_rules):
            return True
    return False


def get_bag_count(bag_colour, bag_rules, current_count):
    for inner_bag_colour in bag_rules[bag_colour].inner_bag_count_by_colour.keys():
        current_count[0] += bag_rules[bag_colour].inner_bag_count_by_colour[
            inner_bag_colour
        ]
        for _ in range(
            bag_rules[bag_colour].inner_bag_count_by_colour[inner_bag_colour]
        ):
            get_bag_count(inner_bag_colour, bag_rules, current_count)


if __name__ == "__main__":
    bag_rules = get_bag_rules("07.txt")
    print(f"Part 1: {part_one(bag_rules)}")
    print(f"Part 2: {part_two(bag_rules)}")