"""
https://adventofcode.com/2022/day/5
"""

from os import linesep
import re
import sys


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.rstrip(linesep) + " " for line in file.readlines()]
    stack_num = len(lines[0]) // 4
    stacks = []
    for j in range(stack_num):
        stacks.append([])
    i = 0
    while "[" in lines[i]:
        for j in range(0, stack_num):
            crate = lines[i][j * 4 + 1]
            if crate.strip():
                stacks[j].append(crate)
        i += 1
    i += 2
    instructions = []
    while i < len(lines):
        match = re.match(r"move (\d+) from (\d+) to (\d+)", lines[i])
        instructions.append(
            [int(match.group(1)), int(match.group(2)), int(match.group(3))]
        )
        i += 1
    return stacks, instructions


def part_one():
    # Stack format: top box appears first
    # Instructions format: move [0] from [1] to [2]
    stacks, instructions = get_data("05.txt")
    for instruction in instructions:
        for _ in range(instruction[0]):
            stacks[instruction[2] - 1].insert(0, stacks[instruction[1] - 1][0])
            del stacks[instruction[1] - 1][0]
    top_crates = ""
    for stack in stacks:
        top_crates += stack[0]
    return top_crates


def part_two():
    # Stack format: top box appears first
    # Instructions format: move [0] from [1] to [2]
    stacks, instructions = get_data("05.txt")
    for instruction in instructions:
        stacks[instruction[2] - 1] = (
            stacks[instruction[1] - 1][: instruction[0]] + stacks[instruction[2] - 1]
        )
        for _ in range(instruction[0]):
            del stacks[instruction[1] - 1][0]
    top_crates = ""
    for stack in stacks:
        top_crates += stack[0]
    return top_crates


if __name__ == "__main__":
    print(part_one())
    print(part_two())
