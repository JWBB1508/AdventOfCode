"""
https://adventofcode.com/2020/day/19
"""

import sys
import re
import copy


class Rule:
    rule_string_re = re.compile(r"^(\d+): (?:((?:\d+[\s|]*)+)|\"(\w)\")$")

    def __init__(self, rule_string):
        self._rule_string = rule_string
        rule_match = Rule.rule_string_re.search(rule_string)
        if not rule_match:
            raise Exception(f"Invalid rule: {rule_string}")
        if not rule_match.group(1) or (
            not rule_match.group(2) and not rule_match.group(3)
        ):
            raise Exception(f"Incomplete rule: {rule_string}")
        if rule_match.group(2) and rule_match.group(3):
            raise Exception(
                f"Rule has groups corresponding to both different kinds of rules: {rule_match.group(2)} and {rule_match.group(3)}"
            )
        self.rule_number = int(rule_match.group(1))
        if rule_match.group(3):
            self.rule_match = rule_match.group(3)
            self.sub_rules = None
        else:
            self.sub_rules = [
                [int(rule_number) for rule_number in section.split(" ") if rule_number]
                for section in rule_match.group(2).split("|")
                if section
            ]
            self.rule_match = None

    def __str__(self):
        return self._rule_string

    def __repr__(self):
        return self._rule_string


def get_data(filename):
    rules_list = []
    messages = []
    with open(f"{sys.path[0]}/../data/{filename}") as file:
        lines = [line.strip() for line in file.readlines()]
    reading_rules = True
    for line in lines:
        if reading_rules:
            if line:
                rules_list.append(Rule(line))
            else:
                reading_rules = False
        else:
            messages.append(line)
    rules = {}
    for rule in rules_list:
        rules[rule.rule_number] = rule
    return rules, messages


def matches_rule(message, rules, rule_number):
    match = _matches_rule(message, rules, rule_number)
    return match[0] and match[1] == len(message)


def _matches_rule(message, rules, rule_number, length_already_matched=0):
    rule = rules[rule_number]
    if rule.rule_match:
        if (
            length_already_matched < len(message)
            and message[length_already_matched] == rule.rule_match
        ):
            length_already_matched += 1
            return True, length_already_matched
        return False, length_already_matched
    else:
        orig_sub_rule_length_already_matched = length_already_matched
        for section in rule.sub_rules:
            valid_for_section = True
            orig_section_length_already_matched = length_already_matched
            for sub_rule_number in section:
                valid_for_section, length_already_matched = _matches_rule(
                    message,
                    rules,
                    sub_rule_number,
                    length_already_matched,
                )
                if not valid_for_section:
                    length_already_matched = orig_section_length_already_matched
                    break
            if valid_for_section:
                return True, length_already_matched
            else:
                length_already_matched = orig_sub_rule_length_already_matched
        return False, length_already_matched


def part_one(data):
    num_matches = 0
    for message in data[1]:
        if matches_rule(message, data[0], 0):
            num_matches += 1
    return num_matches


def part_two(data):
    num_matches = 0
    data[0][8] = Rule("8: 42 | 42 8")
    data[0][11] = Rule("11: 42 31 | 42 11 31")
    for message in data[1]:
        if matches_rule(message, data[0], 0):
            print(message)
            num_matches += 1
    return num_matches


if __name__ == "__main__":
    data = get_data("19.txt")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
