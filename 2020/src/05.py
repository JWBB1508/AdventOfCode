"""
https://adventofcode.com/2020/day/5
"""

import sys


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [line.strip() for line in file.readlines()]


def part_one(data):
    max_seat_id = 0
    for seat in data:
        row = get_row_col(seat[:7], 0, 127)
        column = get_row_col(seat[7:], 0, 7)
        seat_id = (row * 8) + column
        max_seat_id = max(max_seat_id, seat_id)
    return max_seat_id


def part_two(data):
    missing_seats = {(row * 8) + col for row in range(0, 128) for col in range(0, 8)}
    present_seats = set()
    for seat in data:
        row = get_row_col(seat[:7], 0, 127)
        column = get_row_col(seat[7:], 0, 7)
        seat_id = (row * 8) + column
        missing_seats.remove(seat_id)
        present_seats.add(seat_id)
    missing_seats_temp = {seat for seat in missing_seats}
    for seat in missing_seats_temp:
        if seat + 1 not in present_seats or seat - 1 not in present_seats:
            missing_seats.remove(seat)
    if len(missing_seats) != 1:
        raise Exception("Multiple missing seats found!")
    return next(iter(missing_seats))


def get_row_col(code, min, max):
    for char in code:
        if char == "F" or char == "L":
            max = max - ((max - min) // 2) - 1
        elif char == "B" or char == "R":
            min = min + ((max - min) // 2) + 1
        else:
            raise Exception(f"Unexpected character: {char}")
    if min != max:
        raise Exception(
            f"Expected only one possible value, but values are allowed between {min} and {max}"
        )
    return min


if __name__ == "__main__":
    data = get_data("05.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")