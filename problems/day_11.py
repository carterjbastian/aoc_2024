from lib.helpers import get_strings_by_lines, log


def split_stone(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        # split in half
        half = len(str(num)) // 2
        return [int(str(num)[:half]), int(str(num)[half:])]
    else:
        return [num * 2024]


def part_1():
    txt = get_strings_by_lines("11.txt")
    stones_lists = [[int(val)] for val in txt[0].split(" ")]

    total = 0
    for stones in stones_lists:
        cur_stones = stones
        for i in range(25):
            new_stones = []
            for stone in cur_stones:
                new_stones += split_stone(stone)
            cur_stones = new_stones
        total += len(cur_stones)

    return total


def part_2():
    txt = get_strings_by_lines("11.txt")
    stones = [int(val) for val in txt[0].split(" ")]
    log(stones)

    cur_stones = stones
    for i in range(75):
        log(f"Iteration {i}")
        new_stones = []
        for stone in cur_stones:
            new_stones += split_stone(stone)
        cur_stones = new_stones

    return len(cur_stones)
