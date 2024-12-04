from lib.helpers import get_strings_by_lines


def check_right(arr, i, j):
    if j + 4 > len(arr[i]):
        return False

    if arr[i][j + 1] == "M" and arr[i][j + 2] == "A" and arr[i][j + 3] == "S":
        return True

    return False


def check_left(arr, i, j):
    if j < 3:  # Need at least 3 positions to the left
        return False

    if arr[i][j - 1] == "M" and arr[i][j - 2] == "A" and arr[i][j - 3] == "S":
        return True

    return False


def check_up(arr, i, j):
    if i < 3:  # Need at least 3 positions above
        return False

    if arr[i - 1][j] == "M" and arr[i - 2][j] == "A" and arr[i - 3][j] == "S":
        return True

    return False


def check_down(arr, i, j):
    if i + 4 > len(arr):  # Need at least 3 positions below
        return False

    if arr[i + 1][j] == "M" and arr[i + 2][j] == "A" and arr[i + 3][j] == "S":
        return True

    return False


def check_up_right(arr, i, j):
    if i < 3 or j + 4 > len(arr[i]):  # Need 3 positions above and 3 to the right
        return False

    if (
        arr[i - 1][j + 1] == "M"
        and arr[i - 2][j + 2] == "A"
        and arr[i - 3][j + 3] == "S"
    ):
        return True

    return False


def check_up_left(arr, i, j):
    if i < 3 or j < 3:  # Need 3 positions above and 3 to the left
        return False

    if (
        arr[i - 1][j - 1] == "M"
        and arr[i - 2][j - 2] == "A"
        and arr[i - 3][j - 3] == "S"
    ):
        return True

    return False


def check_down_right(arr, i, j):
    if i + 4 > len(arr) or j + 4 > len(
        arr[i]
    ):  # Need 3 positions below and 3 to the right
        return False

    if (
        arr[i + 1][j + 1] == "M"
        and arr[i + 2][j + 2] == "A"
        and arr[i + 3][j + 3] == "S"
    ):
        return True

    return False


def check_down_left(arr, i, j):
    if i + 4 > len(arr) or j < 3:  # Need 3 positions below and 3 to the left
        return False

    if (
        arr[i + 1][j - 1] == "M"
        and arr[i + 2][j - 2] == "A"
        and arr[i + 3][j - 3] == "S"
    ):
        return True

    return False


def find_matches(arr):
    total = 0
    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            if col == "X":
                if check_right(arr, i, j):
                    total += 1
                if check_left(arr, i, j):
                    total += 1
                if check_up(arr, i, j):
                    total += 1
                if check_down(arr, i, j):
                    total += 1
                if check_up_right(arr, i, j):
                    total += 1
                if check_up_left(arr, i, j):
                    total += 1
                if check_down_right(arr, i, j):
                    total += 1
                if check_down_left(arr, i, j):
                    total += 1

    return total


def part_1():
    input_arr = get_strings_by_lines("4.txt")
    arr = [[c for c in l] for l in input_arr]

    return find_matches(arr)


def find_mas_right(arr, i, j):
    if i + 3 > len(arr) or j + 3 > len(
        arr[i]
    ):  # Need 3 positions below and 3 to the right
        return False

    if (
        arr[i + 1][j + 1] == "A"
        and arr[i + 2][j + 2] == "S"
        and (
            (arr[i][j + 2] == "M" and arr[i + 2][j] == "S")
            or (arr[i][j + 2] == "S" and arr[i + 2][j] == "M")
        )
    ):
        return True


def find_sam_right(arr, i, j):
    if i + 3 > len(arr) or j + 3 > len(
        arr[i]
    ):  # Need 3 positions below and 3 to the right
        return False

    if (
        arr[i + 1][j + 1] == "A"
        and arr[i + 2][j + 2] == "M"
        and (
            (arr[i][j + 2] == "M" and arr[i + 2][j] == "S")
            or (arr[i][j + 2] == "S" and arr[i + 2][j] == "M")
        )
    ):
        return True


def part_2():
    input_arr = get_strings_by_lines("4.txt")
    sum = 0
    arr = [[c for c in l] for l in input_arr]
    new_arr = [["." for _ in l] for l in input_arr]

    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            if col == "M":
                if find_mas_right(arr, i, j):
                    new_arr[i][j] = "M"
                    sum += 1
            elif col == "S":
                if find_sam_right(arr, i, j):
                    new_arr[i][j] = "S"
                    sum += 1

    return sum
