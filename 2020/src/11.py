"""
https://adventofcode.com/2020/day/11
"""

import sys
import copy


def get_chair_map(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    return [[char for char in line] for line in lines]


def part_one(chair_map):
    new_chair_map = copy.deepcopy(chair_map)
    while True:
        changed_chairs = 0
        current_chair_map = copy.deepcopy(new_chair_map)
        for i, row in enumerate(current_chair_map):
            for j, chair in enumerate(row):
                if (
                    chair == "L"
                    and get_occupied_adjacent_seats(current_chair_map, i, j) == 0
                ):
                    new_chair_map[i][j] = "#"
                    changed_chairs += 1
                elif (
                    chair == "#"
                    and get_occupied_adjacent_seats(current_chair_map, i, j) >= 4
                ):
                    new_chair_map[i][j] = "L"
                    changed_chairs += 1
        if changed_chairs == 0:
            return get_total_occupied_chairs(current_chair_map)


def part_two(chair_map):
    new_chair_map = copy.deepcopy(chair_map)
    while True:
        changed_chairs = 0
        current_chair_map = copy.deepcopy(new_chair_map)
        for i, row in enumerate(current_chair_map):
            for j, chair in enumerate(row):
                if (
                    chair == "L"
                    and get_occupied_visible_seats(current_chair_map, i, j) == 0
                ):
                    new_chair_map[i][j] = "#"
                    changed_chairs += 1
                elif (
                    chair == "#"
                    and get_occupied_visible_seats(current_chair_map, i, j) >= 5
                ):
                    new_chair_map[i][j] = "L"
                    changed_chairs += 1
        if changed_chairs == 0:
            return get_total_occupied_chairs(current_chair_map)


def get_occupied_adjacent_seats(chair_map, i, j):
    return sum(
        chair == "#"
        for chair in [
            chair_map[i - 1][j] if i > 0 else None,
            chair_map[i + 1][j] if i < len(chair_map) - 1 else None,
            chair_map[i][j - 1] if j > 0 else None,
            chair_map[i][j + 1] if j < len(chair_map[i]) - 1 else None,
            chair_map[i - 1][j - 1] if i > 0 and j > 0 else None,
            chair_map[i - 1][j + 1] if i > 0 and j < len(chair_map[i]) - 1 else None,
            chair_map[i + 1][j - 1] if i < len(chair_map) - 1 and j > 0 else None,
            chair_map[i + 1][j + 1]
            if i < len(chair_map) - 1 and j < len(chair_map[i]) - 1
            else None,
        ]
    )


def get_occupied_visible_seats(chair_map, i, j):
    return sum(
        chair == "#"
        for chair in [
            get_next_chair(chair_map, i, j, -1, 0),
            get_next_chair(chair_map, i, j, 1, 0),
            get_next_chair(chair_map, i, j, 0, -1),
            get_next_chair(chair_map, i, j, 0, 1),
            get_next_chair(chair_map, i, j, -1, -1),
            get_next_chair(chair_map, i, j, -1, 1),
            get_next_chair(chair_map, i, j, 1, -1),
            get_next_chair(chair_map, i, j, 1, 1),
        ]
    )


def get_next_chair(chair_map, i, j, i_step, j_step):
    curr_i = i + i_step
    curr_j = j + j_step
    while (
        curr_i >= 0
        and curr_i < len(chair_map)
        and curr_j >= 0
        and curr_j < len(chair_map[curr_i])
    ):
        if chair_map[curr_i][curr_j] == "L" or chair_map[curr_i][curr_j] == "#":
            return chair_map[curr_i][curr_j]
        else:
            curr_i += i_step
            curr_j += j_step
    return None


def get_total_occupied_chairs(chair_map):
    return sum([sum(chair == "#" for chair in row) for row in chair_map])


if __name__ == "__main__":
    chair_map = get_chair_map("11.txt")
    print(f"Part 1: {part_one(chair_map)}")
    print(f"Part 2: {part_two(chair_map)}")