from lib.helpers import get_strings_by_lines, log


class Node:
    def __init__(self, count: int, value: int):
        self.count = count
        self.value = value
        self.next = None


def print_list(head: Node):
    log("")
    cur = head
    while cur is not None:
        log(f"Stone: {cur.value} ({cur.count})")
        cur = cur.next
    log("")


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
    stones_lists = [int(val) for val in txt[0].split(" ")]

    head = Node(25, stones_lists[0])
    cur = head
    for stone in stones_lists[1:]:
        cur.next = Node(25, stone)
        cur = cur.next

    print_list(head)
    total = 0
    cur = head
    while cur is not None:
        if cur.count <= 0:
            total += 1
            cur = cur.next
            continue

        # Update the current stone
        cur.count -= 1
        if cur.value == 0:
            cur.value = 1
        elif len(str(cur.value)) % 2 == 0:
            num = cur.value
            # split in half
            half = len(str(num)) // 2
            cur.value = int(str(num)[:half])
            # Insert a new node after this one
            split_node = Node(cur.count, int(str(num)[half:]))
            split_node.next = cur.next
            cur.next = split_node
        else:
            cur.value *= 2024

    return total


def part_2():
    txt = get_strings_by_lines("11.txt")
    stones = [int(val) for val in txt[0].split(" ")]
    stone_map = {obj: 1 for obj in stones}
    log(stone_map)

    for i in range(75):
        log(f"Starting Iteration {i}")
        # log(stone_map)
        new_map = {}
        for stone, count in stone_map.items():
            new_stones = split_stone(stone)
            for new_stone in new_stones:
                new_map[new_stone] = new_map.get(new_stone, 0) + count
        stone_map = new_map

    return sum(stone_map.values())
