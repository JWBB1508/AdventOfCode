"""
https://adventofcode.com/2020/day/16
"""

import sys
import re
import copy
from tqdm import tqdm


class Data:
    _range_re = re.compile(r"^(\d+)-(\d+)$")

    def __init__(self, fields, my_ticket, other_tickets):
        self.fields = fields
        self.my_ticket = my_ticket
        self.other_tickets = other_tickets

    def is_valid_ticket(self, ticket):
        for value in ticket:
            if not self.get_valid_fields(value):
                return False
        return True

    def get_valid_fields(self, value):
        valid_fields = []
        for field in self.fields.items():
            for field_range in field[1]:
                if value in Data.get_range(field_range):
                    valid_fields.append(field[0])
        return valid_fields

    def get_valid_positions(field, ticket):
        valid_positions = []
        for i, value in enumerate(ticket):
            for field_range in field[1]:
                if value in Data.get_range(field_range):
                    valid_positions.append(i)
        return valid_positions

    def get_range(field_range):
        match = Data._range_re.search(field_range)
        if not match or not match.group(1) or not match.group(2):
            raise Exception(f"Invalid range: {field_range}")
        return list(range(int(match.group(1)), int(match.group(2)) + 1))


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    fields = {}
    field_re = re.compile(r"^([\w ]+): (\d+-\d+ or \d+-\d+)$")
    i = 0
    while True:
        field_match = field_re.search(lines[i])
        if not field_match:
            break
        fields[field_match.group(1)] = field_match.group(2).split(" or ")
        i += 1
    while lines[i] != "your ticket:":
        i += 1
    i += 1
    my_ticket = [int(value) for value in lines[i].split(",")]
    while lines[i] != "nearby tickets:":
        i += 1
    i += 1
    other_tickets = [[int(value) for value in line.split(",")] for line in lines[i:]]
    return Data(fields, my_ticket, other_tickets)


def part_one(data):
    error_rate = 0
    for ticket in tqdm(data.other_tickets):
        for value in ticket:
            if not data.get_valid_fields(value):
                error_rate += value
    return error_rate


def part_two(orig_data):
    # Remove invalid tickets first
    data = copy.deepcopy(orig_data)
    data.other_tickets = [
        ticket for ticket in data.other_tickets if data.is_valid_ticket(ticket)
    ]
    # Now analyse tickets we know are valid
    field_by_position = {}
    old_fields_solved = 0
    possible_positions_by_field = {}
    with tqdm(total=len(data.fields)) as pbar:
        while True:
            pbar.update(len(field_by_position) - old_fields_solved)
            if len(field_by_position) == len(data.fields):
                break
            old_fields_solved = len(field_by_position)
            for field in tqdm(data.fields.items()):
                if field[0] in field_by_position.values():
                    continue
                if field[0] not in possible_positions_by_field:
                    possible_positions_by_field[field[0]] = list(
                        range(len(data.fields))
                    )
                for position in list(possible_positions_by_field[field[0]]):
                    if position in field_by_position.keys():
                        # Position already assigned
                        possible_positions_by_field[field[0]].remove(position)
                        continue
                    for ticket in [data.my_ticket] + data.other_tickets:
                        if position not in Data.get_valid_positions(field, ticket):
                            possible_positions_by_field[field[0]].remove(position)
                if len(possible_positions_by_field[field[0]]) == 0:
                    raise Exception(f"No possible position for field: {field[0]}")
                if len(possible_positions_by_field[field[0]]) == 1:
                    field_by_position[possible_positions_by_field[field[0]][0]] = field[
                        0
                    ]
    departure_positions = [
        position
        for position in field_by_position.keys()
        if field_by_position[position].startswith("departure")
    ]
    product = 1
    for position in departure_positions:
        product *= data.my_ticket[position]
    return product


if __name__ == "__main__":
    data = get_data("16.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")