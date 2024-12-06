from lib.helpers import get_strings_by_lines, log

CLOCKWISE_TURN = {
    (0, -1): (1, 0),  # Moving up -> moving right
    (1, 0): (0, 1),  # Moving right -> moving down
    (0, 1): (-1, 0),  # Moving down -> moving left
    (-1, 0): (0, -1),  # Moving left -> moving up
}

COUNTERCLOCKWISE_TURN = {
    (0, -1): (-1, 0),  # Moving up -> moving left
    (-1, 0): (0, 1),  # Moving left -> moving down
    (0, 1): (1, 0),  # Moving down -> moving right
    (1, 0): (0, -1),  # Moving right -> moving up
}


def part_1():
    arr_input = get_strings_by_lines("6.txt")
    seen = set()
    obstacles = set()

    init_pos = (0, 0)
    init_vel = (0, 0)
    max_x = len(arr_input[0])
    max_y = len(arr_input)
    for y, row in enumerate(arr_input):
        for x, val in enumerate(row):
            if val == ".":
                continue
            elif val == "#":
                obstacles.add((x, y))
            else:
                if val == "^":
                    init_pos = (x, y)
                    init_vel = (0, -1)
                elif val == ">":
                    init_pos = (x, y)
                    init_vel = (1, 0)
                elif val == "v":
                    init_pos = (x, y)
                    init_vel = (0, 1)
                elif val == "<":
                    init_pos = (x, y)
                    init_vel = (-1, 0)
                else:
                    log(f"Unknown character: {val}")
                    raise Exception(f"Unknown character: {val}")

    pos = init_pos
    vel = init_vel
    while pos[1] >= 0 and pos[0] >= 0 and pos[1] < max_y and pos[0] < max_x:
        log(f"At {pos} moving {vel}")
        seen.add(pos)

        next_pos = (pos[0] + vel[0], pos[1] + vel[1])
        # Check for obstacles
        if next_pos in obstacles:
            # Hit a wall. Turn Clockwise
            log(f"Hit a wall at {next_pos}. Turning clockwise")
            vel = CLOCKWISE_TURN[vel]
        else:
            pos = next_pos

    return len(seen)


def run_simulation(obstacles, init_pos, init_vel, max_x, max_y):
    seen = set()
    pos = init_pos
    vel = init_vel
    while pos[1] >= 0 and pos[0] >= 0 and pos[1] < max_y and pos[0] < max_x:
        log(f"At {pos} moving {vel}")
        if (pos, vel) in seen:
            log(f"Seen {pos} {vel} before")
            return True
        seen.add((pos, vel))

        next_pos = (pos[0] + vel[0], pos[1] + vel[1])
        # Check for obstacles
        if next_pos in obstacles:
            # Hit a wall. Turn Clockwise
            log(f"Hit a wall at {next_pos}. Turning clockwise")
            vel = CLOCKWISE_TURN[vel]
        else:
            pos = next_pos

    return False


def part_2():
    arr_input = get_strings_by_lines("6.txt")
    seen = set()
    obstacles = set()

    init_pos = (0, 0)
    init_vel = (0, 0)
    max_x = len(arr_input[0])
    max_y = len(arr_input)
    for y, row in enumerate(arr_input):
        for x, val in enumerate(row):
            if val == ".":
                continue
            elif val == "#":
                obstacles.add((x, y))
            else:
                if val == "^":
                    init_pos = (x, y)
                    init_vel = (0, -1)
                elif val == ">":
                    init_pos = (x, y)
                    init_vel = (1, 0)
                elif val == "v":
                    init_pos = (x, y)
                    init_vel = (0, 1)
                elif val == "<":
                    init_pos = (x, y)
                    init_vel = (-1, 0)
                else:
                    log(f"Unknown character: {val}")
                    raise Exception(f"Unknown character: {val}")

    count = 0
    print(f"Checking {max_x} {max_y} options")
    for possible_y in range(max_y):
        for possible_x in range(max_x):
            print(f"Checking {possible_x} {possible_y}")
            if possible_x == init_pos[0] and possible_y == init_pos[1]:
                continue
            # Make new set with (possible_x, possible_y) and all the other obstacles
            if run_simulation(
                obstacles | {(possible_x, possible_y)}, init_pos, init_vel, max_x, max_y
            ):
                count += 1

    return count
