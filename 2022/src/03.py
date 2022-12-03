"""
https://adventofcode.com/2022/day/2
"""

import sys
from itertools import groupby

BASE_SCORES = {"X": 1, "Y": 2, "Z": 3}

LOSS_VALUE = 0
DRAW_VALUE = 3
WIN_VALUE = 6


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        moves = [line.strip().split() for line in file.readlines()]
    return moves


def get_score(their_move, my_move):
    if their_move not in ["A", "B", "C"]:
        raise Exception(f"Unrecognised opponent move: {their_move}")
    if my_move not in ["X", "Y", "Z"]:
        raise Exception(f"Unrecognised move: {my_move}")
    score = BASE_SCORES[my_move]
    if my_move == "X":
        if their_move == "A":
            score += DRAW_VALUE
        if their_move == "B":
            score += LOSS_VALUE
        if their_move == "C":
            score += WIN_VALUE
    elif my_move == "Y":
        if their_move == "A":
            score += WIN_VALUE
        if their_move == "B":
            score += DRAW_VALUE
        if their_move == "C":
            score += LOSS_VALUE
    elif my_move == "Z":
        if their_move == "A":
            score += LOSS_VALUE
        if their_move == "B":
            score += WIN_VALUE
        if their_move == "C":
            score += DRAW_VALUE
    return score


def get_move(their_move, outcome):
    if their_move not in ["A", "B", "C"]:
        raise Exception(f"Unrecognised opponent move: {their_move}")
    if outcome not in ["X", "Y", "Z"]:
        raise Exception(f"Unrecognised outcome: {outcome}")
    if outcome == "X":
        if their_move == "A":
            return "Z"
        if their_move == "B":
            return "X"
        if their_move == "C":
            return "Y"
    elif outcome == "Y":
        if their_move == "A":
            return "X"
        if their_move == "B":
            return "Y"
        if their_move == "C":
            return "Z"
    elif outcome == "Z":
        if their_move == "A":
            return "Y"
        if their_move == "B":
            return "Z"
        if their_move == "C":
            return "X"


def part_one():
    moves = get_data("02.txt")
    total_score = 0
    for move in moves:
        total_score += get_score(move[0], move[1])
    return total_score


def part_two():
    moves = get_data("02.txt")
    total_score = 0
    for move in moves:
        total_score += get_score(move[0], get_move(move[0], move[1]))
    return total_score


if __name__ == "__main__":
    print(part_one())
    print(part_two())
