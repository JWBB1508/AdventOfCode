"""
https://adventofcode.com/2020/day/8
"""

import sys
import copy


def get_code_steps(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    return [CodeStep(line[:3], int(line[4:])) for line in lines]


class Code:
    def __init__(self, code_steps, initial_accumulator):
        self.code_steps = code_steps
        self.accumulator = initial_accumulator
        self.step_index = 0

    def run(self):
        """
        Returns a status code: 0 for success, 1 for infinite loop detected
        """
        executed_steps = set()
        while self.step_index not in executed_steps:
            if self.step_index >= len(self.code_steps):
                return 0
            executed_steps.add(self.step_index)
            if self.code_steps[self.step_index].type == "nop":
                # No operation - does nothing
                self.step_index += 1
            elif self.code_steps[self.step_index].type == "jmp":
                # Jump - adjusts step_index
                self.step_index += self.code_steps[self.step_index].value
            elif self.code_steps[self.step_index].type == "acc":
                # Accumulator - adjusts accumulator value
                self.accumulator += self.code_steps[self.step_index].value
                self.step_index += 1
        return 1


class CodeStep:
    def __init__(self, type, value):
        self.type = type
        self.value = value


def part_one(code_steps):
    code = Code(code_steps, 0)
    code.run()
    return code.accumulator


def part_two(code_steps):
    modify_index = 0
    while modify_index < len(code_steps):
        if code_steps[modify_index].type == "nop":
            code_steps[modify_index].type = "jmp"
        elif code_steps[modify_index].type == "jmp":
            code_steps[modify_index].type = "nop"
        else:
            modify_index += 1
            continue
        code = Code(code_steps, 0)
        if code.run() == 0:
            return code.accumulator
        else:
            if code_steps[modify_index].type == "nop":
                code_steps[modify_index].type = "jmp"
            elif code_steps[modify_index].type == "jmp":
                code_steps[modify_index].type = "nop"
            modify_index += 1
            continue
    raise Exception("No modification found to prevent infinite loop")


if __name__ == "__main__":
    code_steps = get_code_steps("08.txt")
    print(f"Part 1: {part_one(code_steps)}")
    print(f"Part 2: {part_two(code_steps)}")