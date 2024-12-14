from lib.helpers import get_strings_by_lines, log


def part_1():
    txt = get_strings_by_lines("12.txt")
    # Mapping the index to the region
    accounted_for = {}
    max_y = len(txt)
    max_x = len(txt[0])
    log(f"{max_y}, {max_x}")

    # Map IDs to points + the perimeter
    region_map = {}

    region_idx = 0
    for y, line in enumerate(txt):
        for x, char in enumerate(line):
            # Check if the character is already in a region
            if (x, y) in accounted_for:
                continue

            # Otherwise, we're going to form a new region
            region_char = char
            region_id = f"{region_idx}-{region_char}"
            region_idx += 1
            all_points = []
            additions = [(x, y)]
            accounted_for[(x, y)] = region_id
            perimeter = 0
            log(f"Starting region {region_id} at {x}, {y}")
            while len(additions) > 0:
                log(f"Adding {len(additions)} points")
                cur_point = additions.pop(0)
                # Add to all_points and mark as accounted for
                all_points.append(cur_point)
                cx, cy = cur_point

                # For each direction
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = cx + dx, cy + dy
                    # This point is part of the region
                    if (
                        0 <= nx < max_x
                        and 0 <= ny < max_y
                        and txt[ny][nx] == region_char
                    ):
                        # This point is part of the region, but only add it if it's not already accounted for
                        if (nx, ny) not in accounted_for:
                            log(f"Adding {nx}, {ny} to region {region_id}")
                            accounted_for[(nx, ny)] = region_id
                            additions.append((nx, ny))
                    else:
                        log(
                            f"Skipping {nx}, {ny} as it's out of bounds or not the right region char"
                        )
                        # We need some perimeter there
                        perimeter += 1

            # Done with this region - add to region map
            log(f"Region {region_id} has {perimeter} perimeter")
            region_map[region_id] = (all_points, perimeter)

    log("Accounted for:")
    log(accounted_for)
    log("Region map:")
    log(region_map)

    total_cost = 0
    for region_id, (points, perimeter) in region_map.items():
        log(f"Region {region_id} has {perimeter} perimeter")
        log(f"Points: {points}")
        log(f"Cost: {len(points) * perimeter}")
        total_cost += len(points) * perimeter

    log(f"Total cost: {total_cost}")

    return total_cost


def part_2():
    txt = get_strings_by_lines("12.txt")
    # Mapping the index to the region
    accounted_for = {}
    max_y = len(txt)
    max_x = len(txt[0])
    log(f"{max_y}, {max_x}")

    # Map IDs to points + the perimeter
    region_map = {}

    region_idx = 0
    for y, line in enumerate(txt):
        for x, char in enumerate(line):
            # Check if the character is already in a region
            if (x, y) in accounted_for:
                continue

            # Otherwise, we're going to form a new region
            region_char = char
            region_id = f"{region_idx}-{region_char}"
            region_idx += 1
            all_points = []
            additions = [(x, y)]
            accounted_for[(x, y)] = region_id
            perimeter = 0
            log(f"Starting region {region_id} at {x}, {y}")
            while len(additions) > 0:
                log(f"Adding {len(additions)} points")
                cur_point = additions.pop(0)
                # Add to all_points and mark as accounted for
                all_points.append(cur_point)
                cx, cy = cur_point

                # For each direction
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = cx + dx, cy + dy
                    # This point is part of the region
                    if (
                        0 <= nx < max_x
                        and 0 <= ny < max_y
                        and txt[ny][nx] == region_char
                    ):
                        # This point is part of the region, but only add it if it's not already accounted for
                        if (nx, ny) not in accounted_for:
                            log(f"Adding {nx}, {ny} to region {region_id}")
                            accounted_for[(nx, ny)] = region_id
                            additions.append((nx, ny))
                    else:
                        log(
                            f"Skipping {nx}, {ny} as it's out of bounds or not the right region char"
                        )
                        # We need some perimeter there
                        perimeter += 1

            # Done with this region - add to region map
            log(f"Region {region_id} has {perimeter} perimeter")
            region_map[region_id] = (all_points, perimeter)

    log("Accounted for:")
    log(accounted_for)
    log("Region map:")
    log(region_map)

    left_side_counts = {}
    for region_id, (points, perimeter) in region_map.items():
        side_idx = 1
        log(f"Looking for left sides in Region {region_id}")
        side_mapping = {}
        for x in range(max_x):
            new_sides = []
            for y in range(max_y):
                if (x, y) not in points:
                    continue

                # Check the square to your left
                if (x - 1, y) in points:
                    # If the square to your left is part of this side, you're on the this side too
                    side_mapping[(x, y)] = side_mapping[(x - 1, y)]
                else:
                    # If the sqaure above you is a part of a _new_ side, you're on that side too
                    if (x, y - 1) in side_mapping and side_mapping[
                        (x, y - 1)
                    ] in new_sides:
                        log(f"Adding {x}, {y} to {side_mapping[(x, y - 1)]}")
                        log(f"New sides: {new_sides}")
                        side_mapping[(x, y)] = side_mapping[(x, y - 1)]
                    else:
                        # Otherwise, this is a new side
                        new_sides.append(side_idx)
                        side_mapping[(x, y)] = side_idx
                        side_idx += 1

        log("Side Mapping:")
        log(side_mapping)
        log(f"Region {region_id} has {max(side_mapping.values())} left sides")
        left_side_counts[region_id] = max(side_mapping.values())

    # Add right side counting
    right_side_counts = {}
    for region_id, (points, perimeter) in region_map.items():
        side_idx = 1
        log(f"Looking for right sides in Region {region_id}")
        side_mapping = {}
        for x in range(max_x - 1, -1, -1):  # Iterate from right to left
            new_sides = []
            for y in range(max_y):
                if (x, y) not in points:
                    continue

                # Check the square to your right
                if (x + 1, y) in points:
                    # If the square to your right is part of this side, you're on this side too
                    side_mapping[(x, y)] = side_mapping[(x + 1, y)]
                else:
                    # If the square above you is part of a _new_ side, you're on that side too
                    if (x, y - 1) in side_mapping and side_mapping[
                        (x, y - 1)
                    ] in new_sides:
                        side_mapping[(x, y)] = side_mapping[(x, y - 1)]
                    else:
                        # Otherwise, this is a new side
                        new_sides.append(side_idx)
                        side_mapping[(x, y)] = side_idx
                        side_idx += 1

        log("Right Side Mapping:")
        log(side_mapping)
        log(f"Region {region_id} has {max(side_mapping.values())} right sides")
        right_side_counts[region_id] = max(side_mapping.values())

    # Add top side counting
    top_side_counts = {}
    for region_id, (points, perimeter) in region_map.items():
        side_idx = 1
        log(f"Looking for top sides in Region {region_id}")
        side_mapping = {}
        for y in range(max_y):  # Iterate from top to bottom
            new_sides = []
            for x in range(max_x):
                if (x, y) not in points:
                    continue

                # Check the square above you
                if (x, y - 1) in points:
                    # If the square above is part of this side, you're on this side too
                    side_mapping[(x, y)] = side_mapping[(x, y - 1)]
                else:
                    # If the square to your left is part of a _new_ side, you're on that side too
                    if (x - 1, y) in side_mapping and side_mapping[
                        (x - 1, y)
                    ] in new_sides:
                        side_mapping[(x, y)] = side_mapping[(x - 1, y)]
                    else:
                        # Otherwise, this is a new side
                        new_sides.append(side_idx)
                        side_mapping[(x, y)] = side_idx
                        side_idx += 1

        log("Top Side Mapping:")
        log(side_mapping)
        log(f"Region {region_id} has {max(side_mapping.values())} top sides")
        top_side_counts[region_id] = max(side_mapping.values())

    # Add bottom side counting
    bottom_side_counts = {}
    for region_id, (points, perimeter) in region_map.items():
        side_idx = 1
        log(f"Looking for bottom sides in Region {region_id}")
        side_mapping = {}
        for y in range(max_y - 1, -1, -1):  # Iterate from bottom to top
            new_sides = []
            for x in range(max_x):
                if (x, y) not in points:
                    continue

                # Check the square below you
                if (x, y + 1) in points:
                    # If the square below is part of this side, you're on this side too
                    side_mapping[(x, y)] = side_mapping[(x, y + 1)]
                else:
                    # If the square to your left is part of a _new_ side, you're on that side too
                    if (x - 1, y) in side_mapping and side_mapping[
                        (x - 1, y)
                    ] in new_sides:
                        side_mapping[(x, y)] = side_mapping[(x - 1, y)]
                    else:
                        # Otherwise, this is a new side
                        new_sides.append(side_idx)
                        side_mapping[(x, y)] = side_idx
                        side_idx += 1

        log("Bottom Side Mapping:")
        log(side_mapping)
        log(f"Region {region_id} has {max(side_mapping.values())} bottom sides")
        bottom_side_counts[region_id] = max(side_mapping.values())

    # Count the left sides of each region
    total_cost = 0
    for region_id, (points, perimeter) in region_map.items():
        # Sum the left, right, top, and bottom sides
        total_sides = (
            left_side_counts[region_id]
            + right_side_counts[region_id]
            + top_side_counts[region_id]
            + bottom_side_counts[region_id]
        )
        log(f"Region {region_id} has {total_sides} total_sides")
        log(f"Points: {points}")
        log(f"Cost: {len(points) * total_sides}")
        total_cost += len(points) * total_sides

    log(f"Total cost: {total_cost}")

    return total_cost
