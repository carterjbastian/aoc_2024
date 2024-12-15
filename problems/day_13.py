from lib.helpers import get_input, log


def kramers_rule(prize_x, prize_y, a_x, a_y, b_x, b_y, offset):
    target_x, target_y = prize_x + offset, prize_y + offset
    determinant = (a_x * b_y) - (a_y * b_x)
    # Solve for A and B rounded to the nearest integer
    A = round(((target_x * b_y) - (target_y * b_x)) / determinant)
    B = round(((a_x * target_y) - (a_y * target_x)) / determinant)
    log(f"target_x: {target_x}, target_y: {target_y}")
    if a_x * A + b_x * B != target_x:
        log(f"No Solution: a_x * A + b_x * B != target_x, A: {A}, B: {B}")
        return -1, -1
    if a_y * A + b_y * B != target_y:
        log(f"No Solution: a_y * A + b_y * B != target_y, A: {A}, B: {B}")
        return -1, -1
    return A, B


def part_1():
    txt = get_input("13.txt")
    machine_strs = txt.split("\n\n")
    offset = 0

    total_cost = 0
    for i, machine_str in enumerate(machine_strs):
        log(f"\nMachine {i}\n")
        mach_a, mach_b, prize = machine_str.split("\n")
        mach_a = mach_a[12:]
        mach_a_x, mach_a_y = mach_a.split(", Y+")
        mach_a_x = int(mach_a_x)
        mach_a_y = int(mach_a_y)
        log(f"mach_a_x: {mach_a_x}, mach_a_y: {mach_a_y}")
        mach_b = mach_b[12:]
        mach_b_x, mach_b_y = mach_b.split(", Y+")
        mach_b_x = int(mach_b_x)
        mach_b_y = int(mach_b_y)
        log(f"mach_b_x: {mach_b_x}, mach_b_y: {mach_b_y}\n")
        prize = prize[9:]
        prize_x, prize_y = prize.split(", Y=")
        prize_x = int(prize_x)
        prize_y = int(prize_y)

        # Start here:
        A, B = kramers_rule(
            prize_x, prize_y, mach_a_x, mach_a_y, mach_b_x, mach_b_y, offset
        )
        log(f"A: {A}, B: {B}")
        if A < 0:
            log(f"No Solution: A < 0, A: {A}, B: {B}")
            continue
        if B < 0:
            log(f"No Solution: B < 0, A: {A}, B: {B}")
            continue

        log(f"Found solution: A: {A}, B: {B}")
        total_cost += (A * 3) + B

    return total_cost


def get_factors(n):
    factors = []
    # Find upper bound for factors (sqrt(n))
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors


def part_2():
    offset = 10000000000000
    txt = get_input("13.txt")
    machine_strs = txt.split("\n\n")

    total_cost = 0
    for i, machine_str in enumerate(machine_strs):
        log(f"\nMachine {i}\n")
        mach_a, mach_b, prize = machine_str.split("\n")
        mach_a = mach_a[12:]
        mach_a_x, mach_a_y = mach_a.split(", Y+")
        mach_a_x = int(mach_a_x)
        mach_a_y = int(mach_a_y)
        log(f"mach_a_x: {mach_a_x}, mach_a_y: {mach_a_y}")
        mach_b = mach_b[12:]
        mach_b_x, mach_b_y = mach_b.split(", Y+")
        mach_b_x = int(mach_b_x)
        mach_b_y = int(mach_b_y)
        log(f"mach_b_x: {mach_b_x}, mach_b_y: {mach_b_y}\n")
        prize = prize[9:]
        prize_x, prize_y = prize.split(", Y=")
        prize_x = int(prize_x)
        prize_y = int(prize_y)

        # Start here:
        A, B = kramers_rule(
            prize_x, prize_y, mach_a_x, mach_a_y, mach_b_x, mach_b_y, offset
        )
        log(f"A: {A}, B: {B}")
        if A < 0:
            log(f"No Solution: A < 0, A: {A}, B: {B}")
            continue
        if B < 0:
            log(f"No Solution: B < 0, A: {A}, B: {B}")
            continue

        log(f"Found solution: A: {A}, B: {B}")
        total_cost += (A * 3) + B

    return total_cost
