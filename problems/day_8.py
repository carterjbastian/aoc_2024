from lib.helpers import get_strings_by_lines, log


def part_1():
    txt = get_strings_by_lines("8.txt")
    nodes = {}
    row_len = len(txt[0])
    col_len = len(txt)
    for y, row in enumerate(txt):
        for x, col in enumerate(row):
            if col == ".":
                continue
            else:
                cur_list = nodes.get(col, [])
                nodes[col] = cur_list + [(x, y)]

    log(row_len)
    log(col_len)
    log(nodes)

    antinodes = {}
    # Loop through each list of nodes
    for node, coords in nodes.items():
        antinodes[node] = []
        # Loop through each combination of two coordinates
        # Start at p1
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                p1_x, p1_y = coords[i]
                p2_x, p2_y = coords[j]
                dx = p1_x - p2_x
                dy = p1_y - p2_y
                cx, cy = p1_x + dx, p1_y + dy
                while 0 <= cx < row_len and 0 <= cy < col_len:
                    antinodes[node] += [(cx, cy)]
                    cx += dx
                    cy += dy
                    break

                cx, cy = p2_x - dx, p2_y - dy
                while 0 <= cx < row_len and 0 <= cy < col_len:
                    antinodes[node] += [(cx, cy)]
                    cx -= dx
                    cy -= dy
                    break

    log(antinodes)

    valid = set()
    for node, coords in antinodes.items():
        for x, y in coords:
            if 0 <= x < row_len and 0 <= y < col_len:
                valid.add((x, y))

    log(valid)
    return len(valid)


def part_2():
    txt = get_strings_by_lines("8.txt")
    nodes = {}
    row_len = len(txt[0])
    col_len = len(txt)
    for y, row in enumerate(txt):
        for x, col in enumerate(row):
            if col == ".":
                continue
            else:
                cur_list = nodes.get(col, [])
                nodes[col] = cur_list + [(x, y)]

    log(row_len)
    log(col_len)
    log(nodes)

    antinodes = {}
    # Loop through each list of nodes
    for node, coords in nodes.items():
        antinodes[node] = []
        # Loop through each combination of two coordinates
        # Start at p1
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                p1_x, p1_y = coords[i]
                p2_x, p2_y = coords[j]
                dx = p2_x - p1_x
                dy = p2_y - p1_y
                cx, cy = p1_x + dx, p1_y + dy
                while 0 <= cx < row_len and 0 <= cy < col_len:
                    antinodes[node] += [(cx, cy)]
                    cx += dx
                    cy += dy

                cx, cy = p2_x - dx, p2_y - dy
                while 0 <= cx < row_len and 0 <= cy < col_len:
                    antinodes[node] += [(cx, cy)]
                    cx -= dx
                    cy -= dy

    log(antinodes)

    valid = set()
    for node, coords in antinodes.items():
        for x, y in coords:
            if 0 <= x < row_len and 0 <= y < col_len:
                valid.add((x, y))

    log(valid)
    return len(valid)
