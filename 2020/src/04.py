"""
https://adventofcode.com/2020/day/4
"""

import sys
import re


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        contents = file.read()
    serial_data = [data.replace("\n", " ") for data in contents.split(f"\n\n")]
    dict_data = []
    for serial_entry in serial_data:
        passport_data = {}
        sections = serial_entry.split(" ")
        for section in sections:
            key_value = section.split(":")
            passport_data[key_value[0]] = key_value[1]
        dict_data.append(passport_data)
    return dict_data


def part_one(data):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    valid_passports = 0
    for passport in data:
        valid = True
        for field in required_fields:
            if field not in passport:
                valid = False
                break
        if valid:
            valid_passports += 1
    return valid_passports


def part_two(data):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    valid_passports = 0
    for passport in data:
        valid = True
        for field in required_fields:
            if field not in passport or not (validate_field(field, passport[field])):
                valid = False
                break
        if valid:
            valid_passports += 1
    return valid_passports


def validate_field(field, value):
    if field == "byr":
        return int_validate(value, 1920, 2002, 4)
    if field == "iyr":
        return int_validate(value, 2010, 2020, 4)
    if field == "eyr":
        return int_validate(value, 2020, 2030, 4)
    if field == "hgt":
        if value[-2:] == "cm":
            return int_validate(value[:-2], 150, 193)
        elif value[-2:] == "in":
            return int_validate(value[:-2], 59, 76)
        else:
            return False
    if field == "hcl":
        regex = re.compile(r"^#[0-9a-f]{6}$")
        return regex.match(value) is not None
    if field == "ecl":
        return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if field == "pid":
        regex = re.compile(r"^[0-9]{9}$")
        return regex.match(value) is not None


def int_validate(value, min, max, digits=None):
    try:
        int_val = int(value)
    except:
        return False
    if int_val < min or int_val > max:
        return False
    if digits is not None and len(value) != digits:
        return False
    return True


if __name__ == "__main__":
    data = get_data("04.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
