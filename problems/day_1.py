import re

from lib.helpers import get_all_strings_by_lines, log


def part_1():
    input_arr = get_all_strings_by_lines("1.txt")
    log(input_arr)

    cur_prod = 0
    for val in input_arr:
        # Get the digits
        digits = re.findall(r"\d", val)
        # Conver with the ~decimal~ system wow!
        d = (int(digits[0]) * 10) + (int(digits[-1]))
        cur_prod += d

    return cur_prod


def part_2():
    input_arr = get_all_strings_by_lines("1.txt")
    log(input_arr)

    cur_prod = 0
    for val in input_arr:
        # Just replace each word with the word, the digit, and then the word again.
        # This will keep any words that share letters from getting broken up.
        numbered = re.sub(r"one", "on1e", val, flags=re.S)
        numbered = re.sub(r"two", "t2wo", numbered, flags=re.S)
        numbered = re.sub(r"three", "thr3ee", numbered, flags=re.S)
        numbered = re.sub(r"four", "fo4ur", numbered, flags=re.S)
        numbered = re.sub(r"five", "fi5ve", numbered, flags=re.S)
        numbered = re.sub(r"six", "si6x", numbered, flags=re.S)
        numbered = re.sub(r"seven", "se7ven", numbered, flags=re.S)
        numbered = re.sub(r"eight", "ei8ght", numbered, flags=re.S)
        numbered = re.sub(r"nine", "ni9ne", numbered, flags=re.S)

        # Use same regex as before to get a list of just the digits
        digits = re.findall(r"\d", numbered)
        log(digits)
        d = (int(digits[0]) * 10) + (int(digits[-1]))
        cur_prod += d

    return cur_prod
