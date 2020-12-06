"""
https://adventofcode.com/2020/day/6
"""

import sys


def get_data(filename):
    """Returns a list of lists: answers per person per group
    e.g.
    [['abc', 'a', 'bx'], ['a', 'y']]
    For two groups: one of three people, one of two people"""
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    answers = [[]]
    group = 0
    for line in lines:
        if line == "":
            answers.append([])
            group += 1
            continue
        answers[group].append(line)
    return answers


def part_one(data):
    sum_yes_answers = 0
    for group in data:
        yes_answers = set()
        for answer in group:
            for char in answer:
                yes_answers.add(char)
        sum_yes_answers += len(yes_answers)
    return sum_yes_answers


def part_two(data):
    sum_yes_answers = 0
    for group in data:
        shared_yes_answers = None
        for answer in group:
            yes_answers = set([char for char in answer])
            shared_yes_answers = (
                yes_answers.intersection(shared_yes_answers)
                if shared_yes_answers is not None
                else yes_answers
            )
        sum_yes_answers += len(shared_yes_answers)
    return sum_yes_answers


if __name__ == "__main__":
    data = get_data("06.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")