from lib.helpers import log, get_all_strings_by_lines

def part_1():
    input_arr = get_all_strings_by_lines('4.txt')
    sum = 0
    for line in input_arr:
        str = line.split(': ')[1]
        win_str, num_str = str.split(' | ')
        win_numbers = [int(x) for x in win_str.split(' ') if x != '']
        numbers = [int(x) for x in num_str.split(' ') if x != '']

        val = 0
        for winner in win_numbers:
            if winner in numbers:
                val += 1
        
        sum += 2 ** (val - 1) if val > 0 else 0
    
    return sum



def part_2():
    input_arr = get_all_strings_by_lines('4.txt')
    values = []
    for line in input_arr:
        str = line.split(': ')[1]
        win_str, num_str = str.split(' | ')
        win_numbers = [int(x) for x in win_str.split(' ') if x != '']
        numbers = [int(x) for x in num_str.split(' ') if x != '']

        val = 0
        for winner in win_numbers:
            if winner in numbers:
                val += 1
        
        values.append(val)
    
    log(values)

    counts = { i: 1 for i in range(len(values)) }
    for idx, val in enumerate(values):
        log(counts)
        current_count = counts[idx]
        for delta in range(1, val + 1):
            counts[idx + delta] = counts[idx+delta] + current_count
    
    log(counts)
    sum = 0
    for count in counts.values():
        sum += count

    return sum