from lib.helpers import get_all_strings_by_lines, log


def part_1():
    input_arr = get_all_strings_by_lines("1.txt")
    log(input_arr)
    numbers = [line.split("   ") for line in input_arr]
    log(numbers)
    left_side = []
    right_side = []
    for x, y in numbers:
        left_side.append(int(x))
        right_side.append(int(y))

    left_side.sort()
    right_side.sort()
    log(left_side)
    log(right_side)

    cur_prod = 0
    for i in range(len(left_side)):
        cur_prod += abs(left_side[i] - right_side[i])

    return cur_prod


def part_2():
    input_arr = get_all_strings_by_lines("1.txt")
    log(input_arr)
    numbers = [line.split("   ") for line in input_arr]
    log(numbers)
    left_side = []
    right_side = []
    for x, y in numbers:
        left_side.append(int(x))
        right_side.append(int(y))

    log(left_side)
    counts = {}
    for y in right_side:
        counts[y] = counts.get(y, 0) + 1

    log(counts)
    sim_score = 0
    for x in left_side:
        sim_score += x * counts.get(x, 0)

    return sim_score
