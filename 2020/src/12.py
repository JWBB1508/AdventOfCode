"""
https://adventofcode.com/2020/day/12
"""

import sys


class PartOneInstruction:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.type}{self.value}"

    def process(self, north_pos, east_pos, deg_north):
        if self.type == "N":
            north_pos += self.value
        elif self.type == "S":
            north_pos -= self.value
        elif self.type == "E":
            east_pos += self.value
        elif self.type == "W":
            east_pos -= self.value
        elif self.type == "L":
            if self.value % 90 != 0:
                raise Exception(f"Unsupported turn angle: {self.value}")
            deg_north = (deg_north - self.value) % 360
        elif self.type == "R":
            if self.value % 90 != 0:
                raise Exception(f"Unsupported turn angle: {self.value}")
            deg_north = (deg_north + self.value) % 360
        elif self.type == "F":
            if deg_north == 0:
                north_pos += self.value
            elif deg_north == 90:
                east_pos += self.value
            elif deg_north == 180:
                north_pos -= self.value
            elif deg_north == 270:
                east_pos -= self.value
            else:
                raise Exception(f"Unsupported bearing: {deg_north}")
        return north_pos, east_pos, deg_north


class PartTwoInstruction:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.type}{self.value}"

    def process(
        self, north_pos_waypoint, east_pos_waypoint, north_pos_ship, east_pos_ship
    ):
        if self.type == "N":
            north_pos_waypoint += self.value
        elif self.type == "S":
            north_pos_waypoint -= self.value
        elif self.type == "E":
            east_pos_waypoint += self.value
        elif self.type == "W":
            east_pos_waypoint -= self.value
        elif self.type == "L":
            orig_n, orig_e = north_pos_waypoint, east_pos_waypoint
            if self.value == 90:
                north_pos_waypoint = orig_e
                east_pos_waypoint = -orig_n
            elif self.value == 180:
                north_pos_waypoint = -orig_n
                east_pos_waypoint = -orig_e
            elif self.value == 270:
                north_pos_waypoint = -orig_e
                east_pos_waypoint = orig_n
            else:
                raise Exception(f"Unsupported turn angle: {self.value}")
        elif self.type == "R":
            orig_n, orig_e = north_pos_waypoint, east_pos_waypoint
            if self.value == 90:
                north_pos_waypoint = -orig_e
                east_pos_waypoint = orig_n
            elif self.value == 180:
                north_pos_waypoint = -orig_n
                east_pos_waypoint = -orig_e
            elif self.value == 270:
                north_pos_waypoint = orig_e
                east_pos_waypoint = -orig_n
            else:
                raise Exception(f"Unsupported turn angle: {self.value}")
        elif self.type == "F":
            north_pos_ship += north_pos_waypoint * self.value
            east_pos_ship += east_pos_waypoint * self.value
        return north_pos_waypoint, east_pos_waypoint, north_pos_ship, east_pos_ship


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [line.strip() for line in file.readlines()]


def part_one(data):
    instructions = [PartOneInstruction(line[0], int(line[1:])) for line in data]
    north_pos = 0
    east_pos = 0
    deg_north = 90
    for instruction in instructions:
        north_pos, east_pos, deg_north = instruction.process(
            north_pos, east_pos, deg_north
        )
    return abs(north_pos) + abs(east_pos)


def part_two(data):
    instructions = [PartTwoInstruction(line[0], int(line[1:])) for line in data]
    north_pos_ship = 0
    east_pos_ship = 0
    north_pos_waypoint = 1
    east_pos_waypoint = 10
    for instruction in instructions:
        (
            north_pos_waypoint,
            east_pos_waypoint,
            north_pos_ship,
            east_pos_ship,
        ) = instruction.process(
            north_pos_waypoint, east_pos_waypoint, north_pos_ship, east_pos_ship
        )
    return abs(north_pos_ship) + abs(east_pos_ship)


if __name__ == "__main__":
    data = get_data("12.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")