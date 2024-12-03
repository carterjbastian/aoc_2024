import re

from lib.helpers import get_all_strings_by_lines, get_input, log


def part_1():
    input_arr = get_all_strings_by_lines("3.txt")
    log(len(input_arr))

    sum = 0
    for line in input_arr:
        # Write an re that matches `mul(a,b)` and extract a and b
        matches = re.finditer(r"mul\(([0-9]+),([0-9]+)\)", line)
        for match in matches:
            a = int(match.group(1))
            b = int(match.group(2))
            sum += a * b

    return sum


def part_2():
    input_str = get_input("3.txt")
    sections = input_str.split("don't()")
    re_created = sections[0]
    for section in sections[1:]:
        # Ignore everything up to the first `do()`
        salvage = section.split("do()")[1:]
        re_created += "".join(salvage)

    log(re_created)

    sum = 0
    # Write an re that matches `mul(a,b)` and extract a and b
    matches = re.finditer(r"mul\(([0-9]+),([0-9]+)\)", re_created)
    for match in matches:
        a = int(match.group(1))
        b = int(match.group(2))
        sum += a * b

    return sum
