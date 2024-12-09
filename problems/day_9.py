from lib.helpers import get_input, log


class Node:
    def __init__(self, value: int | None):
        self.index = None
        self.value = value
        self.prev = None
        self.next = None


def print_node(node: Node):
    cur = node
    while cur is not None:
        print(cur.value if cur.value is not None else ".", end="")
        cur = cur.next
    print()


def part_1():
    txt = get_input("9.txt").strip("\n")
    log(txt)
    log(len(txt))

    i = 0
    id = 0
    first = None
    last = None
    first_index = 0
    last_index = 0
    while i < len(txt):
        log(i)
        val_count = int(txt[i])

        for _ in range(val_count):
            new_node = Node(id)
            if first is None:
                first = new_node
                last = new_node
            else:
                new_node.prev = last
                last_index += 1
                last.next = new_node
                last = new_node

        if i + 1 < len(txt):
            empty_count = int(txt[i + 1])
            for _ in range(empty_count):
                last_index += 1
                new_node = Node(None)
                new_node.prev = last
                last.next = new_node
                last = new_node

        i += 2
        id += 1
    head = first
    first_index = 0
    last_index -= 1
    while True:
        # print_node(head)
        log(f"first_index: {first_index}, last_index: {last_index}")
        # Move first forward to next empty node
        while first.value is not None:
            first = first.next
            first_index += 1

        # Move last backward to next non-empty node
        while last.value is None:
            last = last.prev
            last_index -= 1

        # Swap the values for first and last
        if first_index > last_index:
            break
        first.value, last.value = last.value, first.value

    print_node(head)

    checksum = 0
    cur = head
    cur_index = 0
    while True:
        if cur.value is not None:
            checksum += cur.value * (cur_index)
        cur = cur.next
        cur_index += 1
        if cur is None:
            break

    return checksum


def find_empty_size(head: Node, target_size: int, stop_at: int):
    cur = head
    idx = 0
    cur_streak = 0
    while cur is not None:
        if cur.value is None:
            cur_streak += 1
        else:
            cur_streak = 0

        if cur_streak >= target_size:
            return idx - target_size + 1, cur

        cur = cur.next
        idx += 1
        if idx >= stop_at:
            break
    return -1, None


def part_2():
    txt = get_input("9.txt").strip("\n")
    log(txt)
    log(len(txt))

    i = 0
    id = 0
    first = None
    last = None
    first_index = 0
    last_index = 0
    size_map = {}
    while i < len(txt):
        log(i)
        val_count = int(txt[i])

        for _ in range(val_count):
            size_map[id] = val_count
            new_node = Node(id)
            if first is None:
                first = new_node
                last = new_node
            else:
                new_node.prev = last
                last_index += 1
                last.next = new_node
                last = new_node

        if i + 1 < len(txt):
            empty_count = int(txt[i + 1])
            for _ in range(empty_count):
                last_index += 1
                new_node = Node(None)
                new_node.prev = last
                last.next = new_node
                last = new_node

        i += 2
        id += 1

    head = first
    first_index = 0
    last_index -= 1

    while True:
        # print_node(head)

        # Last pointer currently at end of right-most-file to move
        fnum = last.value
        fsize = size_map[last.value]
        log(f"fsize: {fsize}, file_num: {last.value}")

        s_idx, end_block = find_empty_size(head, fsize, last_index)
        if s_idx == -1:
            log("No empty space found for file")
        else:
            log(f"s_idx: {s_idx}, end_block: {end_block}")

            # Swap file into the empty space
            for _ in range(fsize):
                end_block.value, last.value = last.value, end_block.value
                end_block = end_block.prev
                last = last.prev
                last_index -= 1

        if fnum == 1:
            break

        # Move backwards to the end of the next file from the right
        log(f"fnum: {fnum}, last_index: {last_index}")
        while last is not None and last.value != fnum - 1:
            last = last.prev
            last_index -= 1

        if last is None:
            break

    print_node(head)

    checksum = 0
    cur = head
    cur_index = 0
    while True:
        if cur.value is not None:
            checksum += cur.value * (cur_index)
        cur = cur.next
        cur_index += 1
        if cur is None:
            break

    return checksum
