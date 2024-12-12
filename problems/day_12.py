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
    # Calling it now - flood fill
    txt = get_strings_by_lines("12.txt")

    return len(txt)
