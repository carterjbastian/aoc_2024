from lib.helpers import get_strings_by_lines, log

directions = [
    (0, 1),  # Down
    (1, 0),  # Right
    (0, -1),  # Up
    (-1, 0),  # Left
]


def score_trailhead(x, y, grid):
    # Use BFS to find the possible 9s you can reach from this trailhead
    seen = set()
    summits = set()

    bfs_queue = [(x, y)]
    while len(bfs_queue) > 0:
        log("\n\nNext Iteration\n")
        log(f"Queue: {bfs_queue}")
        log(f"Seen: {seen}")
        cur = bfs_queue.pop(0)
        seen.add(cur)
        cx, cy = cur

        self_val = grid[cy][cx]
        if self_val == 9:
            summits.add(cur)
            continue

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                log(f"Checking: {nx}, {ny} for {self_val + 1}")
                if (nx, ny) not in seen and grid[ny][nx] == self_val + 1:
                    log(f"Adding: {nx}, {ny} to queue ({grid[ny][nx]})")
                    bfs_queue += [(nx, ny)]
                else:
                    log(f"Not adding: {nx}, {ny} to queue ({grid[ny][nx]})")

    log(f"\n\nSummits: {summits}")
    return len(summits)


def part_1():
    txt = get_strings_by_lines("10.txt")

    # Make a 2d array of the numbers provided
    max_y = len(txt)
    max_x = len(txt[0])
    grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

    trail_heads = []
    for y, line in enumerate(txt):
        for x, char in enumerate(line):
            grid[y][x] = int(char)
            if char == "0":
                trail_heads.append((x, y))

    print(grid)
    print(trail_heads)
    sum = 0
    for x, y in trail_heads:
        log(f"Trailhead: {x}, {y}")
        score = score_trailhead(x, y, grid)
        sum += score

    return sum


def rate_trailhead(x, y, grid):
    # Use BFS to find the possible 9s you can reach from this trailhead
    summits = []

    bfs_queue = [(x, y)]
    while len(bfs_queue) > 0:
        log("\n\nNext Iteration\n")
        log(f"Queue: {bfs_queue}")
        cur = bfs_queue.pop(0)
        cx, cy = cur

        self_val = grid[cy][cx]
        if self_val == 9:
            summits += [cur]
            continue

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                log(f"Checking: {nx}, {ny} for {self_val + 1}")
                if grid[ny][nx] == self_val + 1:
                    log(f"Adding: {nx}, {ny} to queue ({grid[ny][nx]})")
                    bfs_queue += [(nx, ny)]
                else:
                    log(f"Not adding: {nx}, {ny} to queue ({grid[ny][nx]})")

    log(f"\n\nSummits: {summits}")
    return len(summits)


def part_2():
    txt = get_strings_by_lines("10.txt")

    # Make a 2d array of the numbers provided
    max_y = len(txt)
    max_x = len(txt[0])
    grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

    trail_heads = []
    for y, line in enumerate(txt):
        for x, char in enumerate(line):
            grid[y][x] = int(char)
            if char == "0":
                trail_heads.append((x, y))

    print(grid)
    print(trail_heads)
    sum = 0
    for x, y in trail_heads:
        log(f"Trailhead: {x}, {y}")
        score = rate_trailhead(x, y, grid)
        sum += score

    return sum
