from lib.helpers import log, get_all_strings_by_lines

def is_symbol(c, gear_only=False):
    return c == "*" if gear_only else c not in [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def part_1():
    input_arr = get_all_strings_by_lines('3.txt')
    grid = [[c 
            for c 
            in line] for line in input_arr]
    log(grid)
    width = len(grid[0])
    height = len(grid)
    
    # Not currently in a number
    number_so_far = ''
    in_number = False
    number_in_part = False
    sum = 0
    # Loop through
    for y in range(height):
        # if in number at beginning of line, maybe add it to sum and reset
        if in_number:
            if number_in_part:
                sum += int(number_so_far)
            else:
                log(f'skipping {number_so_far}')

            in_number = False
            number_so_far = ''
            number_in_part = False

        for x in range(width):
            # Currently looking at a number!
            if grid[y][x].isnumeric():
                # Case 1: Continuing the number
                number_so_far += grid[y][x]
                # Case 2: Starting a new number
                if not in_number:
                    in_number = True
                    number_so_far = grid[y][x]
                    number_in_part = False
                    # Check left side for symbols
                    if x > 0:
                        if is_symbol(grid[y][x-1]):
                            number_in_part = True
                        if y > 0 and is_symbol(grid[y-1][x-1]):
                            number_in_part = True
                        if y < height - 1 and is_symbol(grid[y+1][x-1]):
                            number_in_part = True
                if not number_in_part:
                    if y > 0 and is_symbol(grid[y-1][x]):
                        number_in_part = True
                    if y < height - 1 and is_symbol(grid[y+1][x]):
                        number_in_part = True
            else: # Not a digit
                # Case 3: Was in a number - finish it
                if in_number:
                    # Check right side for symbols
                    if x < width - 1:
                        if is_symbol(grid[y][x]):
                            number_in_part = True
                        if y > 0 and is_symbol(grid[y-1][x]):
                            number_in_part = True
                        if y < height - 1 and is_symbol(grid[y+1][x]):
                            number_in_part = True
                    # Maybe add it to sum
                    if number_in_part:
                        sum += int(number_so_far)
                    else:
                        log(f'skipping {number_so_far}')
                    # Reset state
                    in_number = False
                    number_so_far = ''
                    number_in_part = False
                # Case 4: Not in a number and wasn't - do nothing

    return sum


def part_2():
    input_arr = get_all_strings_by_lines('3.txt')
    grid = [[c 
            for c 
            in line] for line in input_arr]
    log(grid)
    width = len(grid[0])
    height = len(grid)
    
    # Not currently in a number
    number_so_far = ''
    in_number = False
    number_in_part = False
    sum = 0

    gear_list = []
    gear_mapping = {}

    # Loop through
    for y in range(height):
        # if in number at beginning of line, maybe add it to sum and reset
        if in_number:
            for gear in gear_list:
                gear_mapping[gear] = gear_mapping[gear] + [number_so_far] if gear in gear_mapping else [number_so_far]
            gear_list = []

            in_number = False
            number_so_far = ''

        for x in range(width):
            # Currently looking at a number!
            if grid[y][x].isnumeric():
                # Case 1: Continuing the number
                number_so_far += grid[y][x]
                # Case 2: Starting a new number
                if not in_number:
                    in_number = True
                    number_so_far = grid[y][x]
                    # Check left side for symbols
                    if x > 0:
                        if is_symbol(grid[y][x-1], gear_only=True):
                            gear_list.append((y, x-1))
                        if y > 0 and is_symbol(grid[y-1][x-1], gear_only=True):
                            gear_list.append((y - 1, x-1))
                        if y < height - 1 and is_symbol(grid[y+1][x-1], gear_only=True):
                            gear_list.append((y + 1, x-1))
                if not number_in_part:
                    if y > 0 and is_symbol(grid[y-1][x], gear_only=True):
                        gear_list.append((y - 1, x))
                    if y < height - 1 and is_symbol(grid[y+1][x], gear_only=True):
                        gear_list.append((y + 1, x))
            else: # Not a digit
                # Case 3: Was in a number - finish it
                if in_number:
                    # Check right side for symbols
                    if x < width - 1:
                        if is_symbol(grid[y][x], gear_only=True):
                            gear_list.append((y, x))
                        if y > 0 and is_symbol(grid[y-1][x], gear_only=True):
                            gear_list.append((y-1, x))
                        if y < height - 1 and is_symbol(grid[y+1][x], gear_only=True):
                            gear_list.append((y+1, x))
                    # Reset state - Add all gear to mapping with number
                    for gear in gear_list:
                        gear_mapping[gear] = gear_mapping[gear] + [number_so_far] if gear in gear_mapping else [number_so_far]

                    gear_list = []
                    in_number = False
                    number_so_far = ''
                # Case 4: Not in a number and wasn't - do nothing

    for gear, numbers in gear_mapping.items():
        if len(numbers) == 2:
            sum += int(numbers[0]) * int(numbers[1])

    return sum