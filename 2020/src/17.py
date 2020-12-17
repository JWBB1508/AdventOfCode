"""
https://adventofcode.com/2020/day/17
"""

import sys
import copy
from itertools import product
from tqdm import tqdm


class ConwayCube:
    def __init__(self, coords, active):
        self.coords = coords
        self.active = active

    def __str__(self):
        return "#" if self.active else "."

    def __repr__(self):
        return f"{','.join(self.coords)}, {self.active}"


class PocketDimension:
    def __init__(self, conway_cubes, dimensions):
        self.conway_cubes = conway_cubes
        self.dimenions = dimensions

    # def __str__(self):
    #     min_coords = [
    #         min([cube.coords[i] for cube in self.conway_cubes.values()])
    #         for i in range(self.dimensions)
    #     ]
    #     max_coords = [
    #         max([cube.coords[i] for cube in self.conway_cubes.values()])
    #         for i in range(self.dimensions)
    #     ]
    #     string = ""
    #     for z in range(min_z, max_z + 1):
    #         string += f"z = {z}\n"
    #         for y in range(min_y, max_y + 1):
    #             for x in range(min_x, max_x + 1):
    #                 string += str(self.get_cube(x, y, z))
    #             string += "\n"
    #         string += "\n"
    #     return string

    def get_key(coords):
        return ",".join([str(coord) for coord in coords])

    def get_cube(self, coords):
        key = PocketDimension.get_key(coords)
        if key not in self.conway_cubes:
            # Add a new inactive cube
            self.conway_cubes[key] = ConwayCube(coords, False)
        return self.conway_cubes[key]

    def set_cube(self, coords, active):
        self.get_cube(coords).active = active

    def cycle(self):
        orig_cubes = copy.deepcopy(self.conway_cubes)
        for cube in orig_cubes.values():
            # Adds a layer of inactive cubes around the outside
            self.get_neighbours(cube.coords)
        orig_cubes = copy.deepcopy(self.conway_cubes)
        cube_updates = {}
        for cube in orig_cubes.values():
            active_neighbours = len(
                [
                    neighbour
                    for neighbour in self.get_neighbours(cube.coords)
                    if neighbour.active
                ]
            )
            key = PocketDimension.get_key(cube.coords)
            if cube.active:
                if active_neighbours != 2 and active_neighbours != 3:
                    cube_updates[key] = False
            else:
                if active_neighbours == 3:
                    cube_updates[key] = True
        for update in cube_updates.items():
            self.conway_cubes[update[0]].active = update[1]

    def get_active_cube_count(self):
        return len([cube for cube in self.conway_cubes.values() if cube.active])

    def get_neighbours(self, coords):
        neighbours = []
        neighbour_coords = [[coord - 1, coord, coord + 1] for coord in coords]
        for neighbour_coords in product(*neighbour_coords):
            for i, coord in enumerate(neighbour_coords):
                if coord != coords[i]:
                    neighbours.append(self.get_cube(neighbour_coords))
                    break
        return neighbours


def get_starting_cubes(filename, dimensions):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    starting_cubes = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            # Starting plane is at z = 0, w = 0
            coords = [j, i] + [0] * (dimensions - 2)
            starting_cubes[PocketDimension.get_key(coords)] = ConwayCube(
                coords, char == "#"
            )
    return starting_cubes


def part_one(starting_cubes):
    pocket_dimension = PocketDimension(starting_cubes, 3)
    for _ in tqdm(range(6)):
        pocket_dimension.cycle()
    return pocket_dimension.get_active_cube_count()


def part_two(starting_cubes):
    pocket_dimension = PocketDimension(starting_cubes, 4)
    for _ in tqdm(range(6)):
        pocket_dimension.cycle()
    return pocket_dimension.get_active_cube_count()


if __name__ == "__main__":
    starting_cubes = get_starting_cubes("17.txt", 3)
    print(f"Part 1: {part_one(starting_cubes)}")
    starting_cubes = get_starting_cubes("17.txt", 4)
    print(f"Part 2: {part_two(starting_cubes)}")