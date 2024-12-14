from lib.helpers import get_input, log


def part_1():
    txt = get_input("13.txt")
    machine_strs = txt.split("\n\n")

    total_cost = 0
    for i, machine_str in enumerate(machine_strs):
        log(f"Machine {i}")
        mach_a, mach_b, prize = machine_str.split("\n")
        mach_a = mach_a[12:]
        mach_a_x, mach_a_y = mach_a.split(", Y+")
        log(f"mach_a_x: {mach_a_x}, mach_a_y: {mach_a_y}")
        mach_b = mach_b[12:]
        mach_b_x, mach_b_y = mach_b.split(", Y+")
        log(f"mach_b_x: {mach_b_x}, mach_b_y: {mach_b_y}")
        prize = prize[9:]
        prize_x, prize_y = prize.split(", Y=")
        log(f"prize_x: {prize_x}, prize_y: {prize_y}")
        log(machine_str)

        # Press the B button (for 1 token) as many times as possible
        b_count = 0
        possible_b_counts = []
        best_config = None
        best_cost = None
        while b_count < 100:
            x_cur = int(mach_b_x) * b_count
            y_cur = int(mach_b_y) * b_count
            if (
                (int(prize_x) - x_cur) % int(mach_a_x) == 0
                and (int(prize_y) - y_cur) % int(mach_a_y) == 0
                and (
                    (int(prize_x) - x_cur) // int(mach_a_x)
                    == (int(prize_y) - y_cur) // int(mach_a_y)
                )
            ):
                a_count = (int(prize_x) - x_cur) // int(mach_a_x)
                log(f"Possible config = {b_count} b-presses + {a_count} a-presses")
                if a_count > 100:
                    log("\ta_count > 100, skipping")
                    continue
                possible_b_counts.append(b_count)
                cost = b_count + (3 * a_count)
                if best_cost is None or cost < best_cost:
                    log("\tcost < best_cost, updating best_cost and best_config")
                    best_cost = cost
                    best_config = (b_count, a_count)

            b_count += 1
        log(f"best_cost: {best_cost}")
        log(f"best_config: {best_config}")
        total_cost += best_cost if best_config is not None else 0

    return total_cost


def get_factors(n):
    factors = []
    # Find upper bound for factors (sqrt(n))
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors


def part_2():
    txt = get_input("13.txt")

    txt = get_input("13.txt")
    machine_strs = txt.split("\n\n")

    total_cost = 0
    for i, machine_str in enumerate(machine_strs):
        log(f"Machine {i}")
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
        log(f"mach_b_x: {mach_b_x}, mach_b_y: {mach_b_y}")
        prize = prize[9:]
        prize_x, prize_y = prize.split(", Y=")
        prize_x = int(prize_x) + 10000000000000
        prize_y = int(prize_y) + 10000000000000
        prize_x_factors = get_factors(prize_x)
        prize_y_factors = get_factors(prize_y)
        log(f"prize_x_factors: {prize_x_factors}")
        log(f"prize_y_factors: {prize_y_factors}")

        # Find the factors of prize_x and prize_y

        log(f"prize_x: {prize_x}, prize_y: {prize_y}")
        log(machine_str)

        # Press the B button (for 1 token) as many times as possible
        possible_b_counts = []
        best_config = None
        best_cost = None
        b_upper_bound = min(prize_x // mach_b_x, prize_y // mach_b_y)
        b_count = b_upper_bound
        print(f"b_upper_bound: {b_upper_bound}")
        while b_count >= 0:
            x_cur = mach_b_x * b_count
            y_cur = mach_b_y * b_count
            if (
                (prize_x - x_cur) % mach_a_x == 0
                and (prize_y - y_cur) % mach_a_y == 0
                and ((prize_x - x_cur) // mach_a_x == (prize_y - y_cur) // mach_a_y)
            ):
                a_count = (prize_x - x_cur) // mach_a_x
                log(f"Possible config = {b_count} b-presses + {a_count} a-presses")
                if a_count > 100:
                    log("\ta_count > 100, skipping")
                    continue
                possible_b_counts.append(b_count)
                cost = b_count + (3 * a_count)
                if best_cost is None or cost < best_cost:
                    log("\tcost < best_cost, updating best_cost and best_config")
                    best_cost = cost
                    best_config = (b_count, a_count)
                    break

            b_count -= 1
        log(f"best_cost: {best_cost}")
        log(f"best_config: {best_config}")
        total_cost += best_cost if best_config is not None else 0

    return total_cost
