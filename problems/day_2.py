from lib.helpers import get_all_strings_by_lines, log


def part_1():
    input_arr = get_all_strings_by_lines("2.txt")
    log(input_arr)

    count = 0
    for line in input_arr:
        numbers = [int(x) for x in line.split(" ")]
        if safe_checker(numbers, safety_run=True):
            count += 1

    log(count)

    return count


def safe_checker(numbers, safety_run=False):
    cur_num = numbers[0]
    dir = None
    for idx, number in enumerate(numbers):
        if idx == 0:
            continue
        if dir is None:
            if number > cur_num:
                dir = "right"
            elif number < cur_num:
                dir = "left"
            else:
                if safety_run:
                    return False
                else:
                    return any(
                        [
                            safe_checker(numbers[1:], safety_run=True),
                            safe_checker([numbers[0]] + numbers[2:], safety_run=True),
                        ]
                    )

        if dir == "right":
            if number not in [cur_num + 1, cur_num + 2, cur_num + 3]:
                if safety_run:
                    return False
                else:
                    if idx == len(numbers) - 1:
                        return True
                    return any(
                        [
                            safe_checker(
                                numbers[0:idx] + numbers[idx + 1 :], safety_run=True
                            ),
                            safe_checker(
                                numbers[0 : idx + 1] + numbers[idx + 2 :],
                                safety_run=True,
                            ),
                        ]
                    )
        elif dir == "left":
            if number not in [cur_num - 1, cur_num - 2, cur_num - 3]:
                if safety_run:
                    return False
                else:
                    if idx == len(numbers) - 1:
                        return True
                    return any(
                        [
                            safe_checker(
                                numbers[0:idx] + numbers[idx + 1 :], safety_run=True
                            ),
                            safe_checker(
                                numbers[0 : idx + 1] + numbers[idx + 2 :],
                                safety_run=True,
                            ),
                        ]
                    )
        cur_num = number

    print(f"safe_checker {numbers} returned True")
    return True


def part_2():
    input_arr = get_all_strings_by_lines("2.txt")
    log(input_arr)
    count = 0
    for line in input_arr:
        numbers = [int(x) for x in line.split(" ")]
        if safe_checker(numbers, safety_run=False) or safe_checker(
            numbers[::-1], safety_run=False
        ):
            count += 1

    log(count)

    return count
