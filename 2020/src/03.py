"""
https://adventofcode.com/2020/day/3
"""

import sys


def get_tree_map(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    return [[True if char == "#" else False for char in line] for line in lines]


def count_trees(tree_map, x_step, y_step):
    x = x_step
    y = y_step
    tree_count = 0
    while y < len(tree_map):
        while x >= len(tree_map[y]):
            x -= len(tree_map[y])
        if tree_map[y][x]:
            tree_count += 1
        x += x_step
        y += y_step
    return tree_count


if __name__ == "__main__":
    tree_map = get_tree_map("03.txt")
    print(f"Part 1: {count_trees(tree_map, 3, 1)}")
    print(
        f"Part 2: {count_trees(tree_map, 1, 1) * count_trees(tree_map, 3, 1) * count_trees(tree_map, 5, 1) * count_trees(tree_map, 7, 1) * count_trees(tree_map, 1, 2)}"
    )
