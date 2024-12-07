from lib.helpers import get_strings_by_lines, log


def p1_test(arr):
    goal = arr[0]
    curr_opts = [arr[1]]
    remaining = arr[2:]

    while len(remaining) > 0:
        log(curr_opts)
        log(remaining)
        new_opts = []
        for x in curr_opts:
            new_opts += [x + remaining[0]] + [x * remaining[0]]

        curr_opts = list(filter(lambda x: x <= goal, new_opts))
        remaining = remaining[1:]

    if goal in curr_opts:
        return True
    else:
        return False


def p2_test(arr):
    goal = arr[0]
    curr_opts = [arr[1]]
    remaining = arr[2:]

    while len(remaining) > 0:
        log(curr_opts)
        log(remaining)
        new_opts = []
        for x in curr_opts:
            new_opts += (
                [x + remaining[0]]
                + [x * remaining[0]]
                + [int(str(x) + str(remaining[0]))]
            )

        curr_opts = list(filter(lambda x: x <= goal, new_opts))
        remaining = remaining[1:]

    if goal in curr_opts:
        return True
    else:
        return False


def part_1():
    txt = get_strings_by_lines("7.txt")
    eqns = []
    for line in txt:
        eqn = []
        num, eq = line.split(": ")
        eqn.append(int(num))
        eqn += [int(x) for x in eq.split(" ")]
        eqns.append(eqn)

    log(eqns)
    sum = 0
    for eqn in eqns:
        if p1_test(eqn):
            sum += eqn[0]

    return sum


def part_2():
    txt = get_strings_by_lines("7.txt")
    eqns = []
    for line in txt:
        eqn = []
        num, eq = line.split(": ")
        eqn.append(int(num))
        eqn += [int(x) for x in eq.split(" ")]
        eqns.append(eqn)

    log(eqns)
    sum = 0
    for eqn in eqns:
        if p2_test(eqn):
            sum += eqn[0]

    return sum
