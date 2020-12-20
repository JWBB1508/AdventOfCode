"""
https://adventofcode.com/2020/day/18
"""

import sys
import re
from enum import Enum


class Precedence(Enum):
    LeftToRight = 1
    AdditionMultiplication = 2


def get_data(filename):
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        return [line.strip() for line in file.readlines()]


def evaluate(expression, precedence):
    expression = expression.strip()
    brackets = get_first_outermost_brackets(expression)
    while brackets:
        expression = expression.replace(
            f"({brackets})", str(evaluate(brackets, precedence))
        )
        brackets = get_first_outermost_brackets(expression)
    # Evaluate expression with no brackets
    if precedence == Precedence.LeftToRight:
        current_value = int(re.search(r"^\d+", expression).group(0))
        components = re.findall(r"[+*]\s*\d+", expression)
        for component in components:
            operator_operand = re.search(r"([+*])\s*([\d]+)", component)
            current_value = apply_operation(
                operator_operand.group(1), current_value, int(operator_operand.group(2))
            )
        return current_value
    elif precedence == Precedence.AdditionMultiplication:
        first_addition_pair = re.search(r"(\d+)\s*\+\s*(\d+)", expression)
        while first_addition_pair:
            expression = re.sub(
                fr"\b{re.escape(first_addition_pair.group(0))}\b",
                str(
                    apply_operation(
                        "+",
                        int(first_addition_pair.group(1)),
                        int(first_addition_pair.group(2)),
                    )
                ),
                expression,
            )
            first_addition_pair = re.search(r"(\d+)\s*\+\s*(\d+)", expression)
        if "+" in expression:
            raise Exception(f"Unparsed addition in expression: {expression}")
        return evaluate(expression, Precedence.LeftToRight)


def get_first_outermost_brackets(expression):
    start_char = None
    bracket_count = 0
    for i, char in enumerate(expression):
        if char == "(":
            if start_char is None:
                start_char = i + 1
            else:
                bracket_count += 1
        if char == ")":
            if bracket_count == 0:
                return expression[start_char:i]
            else:
                bracket_count -= 1
    return None


def apply_operation(operator, first_operand, second_operand):
    if operator == "+":
        return first_operand + second_operand
    if operator == "*":
        return first_operand * second_operand
    raise Exception(f"Unknown operator: {operator}")


def part_one(data):
    sum = 0
    for expression in data:
        sum += evaluate(expression, Precedence.LeftToRight)
    return sum


def part_two(data):
    sum = 0
    for expression in data:
        sum += evaluate(expression, Precedence.AdditionMultiplication)
    return sum


if __name__ == "__main__":
    data = get_data("18.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
