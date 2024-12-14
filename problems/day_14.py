from lib.config import TEST_MODE
from lib.helpers import get_all_strings_by_lines, log


def move_multiple(pos, vel, boundaries, n):
    for _ in range(n):
        pos = move_once(pos, vel, boundaries)
    return pos


def move_once(pos, vel, boundaries):
    pos_x, pos_y = pos
    vel_x, vel_y = vel
    boundaries_x, boundaries_y = boundaries

    pos_x += vel_x
    pos_y += vel_y

    if pos_x >= boundaries_x:
        # Wrap right -> left
        pos_x = pos_x % boundaries_x
    if pos_y >= boundaries_y:
        # Wrap bottom -> top
        pos_y = pos_y % boundaries_y

    if pos_x < 0:
        # Wrap left -> right
        pos_x = boundaries_x + pos_x
    if pos_y < 0:
        # Wrap top -> bottom
        pos_y = boundaries_y + pos_y

    return (pos_x, pos_y)


def calculate_quadrants(bots, boundaries):
    max_x, max_y = boundaries
    quadrants = [0, 0, 0, 0]

    for bot in bots:
        pos_x, pos_y = bot
        if pos_x == max_x // 2 or pos_y == max_y // 2:
            log(f"Skipping {bot} because it's on the boundary")
            continue

        if 0 <= pos_x < max_x // 2:
            # In left quadrant
            if 0 <= pos_y < max_y // 2:
                # In upper quadrant
                quadrants[0] += 1
            else:
                # In lower quadrant
                quadrants[1] += 1
        else:
            # In right quadrant
            if 0 <= pos_y < max_y // 2:
                # In upper quadrant
                quadrants[2] += 1
            else:
                # In lower quadrant
                quadrants[3] += 1

    log(
        f"Quadrant counts: {quadrants[0]} -> {quadrants[2]} -> {quadrants[3]} -> {quadrants[1]}"
    )
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part_1():
    input_arr = get_all_strings_by_lines("14.txt")
    boundaries = (11, 7) if TEST_MODE else (101, 103)
    bots = []
    vels = []
    for idx, line in enumerate(input_arr, start=1):
        p_str, v_str = line.split(" v=")
        p_x, p_y = [int(x) for x in p_str[2:].split(",")]
        v_x, v_y = [int(x) for x in v_str.split(",")]
        bots += [(p_x, p_y)]
        vels += [(v_x, v_y)]
        log(f"{idx}: ({p_x}, {p_y}), velocity: ({v_x}, {v_y}")

    print("Bots: ", bots)
    print("Vels: ", vels)
    print("Boundaries: ", boundaries)
    print(calculate_quadrants(bots, boundaries))
    n = 100
    after_bots = []
    for idx, bot in enumerate(bots):
        after_bots.append(move_multiple(bot, vels[idx], boundaries, n))

    return calculate_quadrants(after_bots, boundaries)


def print_bots(bots, boundaries):
    max_x, max_y = boundaries
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in bots:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part_2():
    input_arr = get_all_strings_by_lines("14.txt")
    boundaries = (11, 7) if TEST_MODE else (101, 103)
    bots = []
    vels = []
    for idx, line in enumerate(input_arr, start=1):
        p_str, v_str = line.split(" v=")
        p_x, p_y = [int(x) for x in p_str[2:].split(",")]
        v_x, v_y = [int(x) for x in v_str.split(",")]
        bots += [(p_x, p_y)]
        vels += [(v_x, v_y)]
        log(f"{idx}: ({p_x}, {p_y}), velocity: ({v_x}, {v_y}")

    print("Bots: ", bots)
    print("Vels: ", vels)
    print("Boundaries: ", boundaries)
    print(calculate_quadrants(bots, boundaries))
    n = 10000
    after_bots = []
    for i in range(n):
        print("=" * 100)
        print(f"\nIteration {i}\n")
        print_bots(bots, boundaries)
        for idx, bot in enumerate(bots):
            after_bots.append(move_multiple(bot, vels[idx], boundaries, 1))
        bots = after_bots
        after_bots = []
        print("=" * 100)
