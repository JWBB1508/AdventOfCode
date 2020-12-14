"""
https://adventofcode.com/2020/day/14
"""

import sys
import re


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [line.strip() for line in file.readlines()]


def part_one(data):
    mask = None
    mem_regex = re.compile(r"^mem\[(\d+)\] = (\d+)$")
    memory = {}
    for line in data:
        if line[0:7] == "mask = ":
            mask = line[7:]
        else:
            match = mem_regex.search(line)
            address = int(match.group(1))
            value = int(match.group(2))
            memory[address] = apply_mask_to_value(mask, value)
    return sum(memory.values())


def part_two(data):
    mask = None
    mem_regex = re.compile(r"^mem\[(\d+)\] = (\d+)$")
    memory = {}
    for line in data:
        if line[0:7] == "mask = ":
            mask = line[7:]
        else:
            match = mem_regex.search(line)
            base_address = apply_mask_to_address(mask, int(match.group(1)))
            value = int(match.group(2))
            for address in get_addresses_from_base(base_address):
                memory[address] = value
    return sum(memory.values())


def apply_mask_to_value(mask, value):
    if mask is None:
        raise Exception("Mask not set")
    # Remove 0b prefix and pad
    value_chars = list(bin(value))[2:]
    value_chars = ["0"] * (len(mask) - len(value_chars)) + value_chars
    for i, char in enumerate(mask):
        if char == "X":
            continue
        value_chars[i] = char
    return int("".join(value_chars), 2)


def apply_mask_to_address(mask, address):
    if mask is None:
        raise Exception("Mask not set")
    # Remove 0b prefix and pad
    address_chars = list(bin(address))[2:]
    address_chars = ["0"] * (len(mask) - len(address_chars)) + address_chars
    for i, char in enumerate(mask):
        if char == "0":
            continue
        address_chars[i] = char
    return "".join(address_chars)


def get_addresses_from_base(address):
    addresses = set()
    x_count = 0
    x_indices = []
    for i, char in enumerate(address):
        if char == "X":
            x_count += 1
            x_indices.append(i)
    for value in range(2 ** x_count):
        temp_address = list(address)
        value_str = list(bin(value)[2:])
        value_str = ["0"] * (x_count - len(value_str)) + value_str
        for i, char in enumerate(value_str):
            temp_address[x_indices[i]] = char
        addresses.add("".join(temp_address))
    return addresses


if __name__ == "__main__":
    data = get_data("14.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")