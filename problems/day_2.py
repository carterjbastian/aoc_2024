from lib.helpers import log, get_all_strings_by_lines

def part_1():
    config = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    input_arr = get_all_strings_by_lines('2.txt')
    log(input_arr)

    game = 1
    sum = 0
    for val in input_arr:
        possible = True
        sets = val.split('; ')
        for s in sets:
            pulls = s.split(', ')
            for pull in pulls:
                count_s, color = pull.split(' ')
                count = int(count_s)
                # log(f'Game {game}: {s}: {pull}: {count} {color}')
                if count > config[color]:
                    log(f'Game {game}: {color} is over the limit!')
                    possible = False

        if possible:
            log(f'Game {game} is possible!')
            sum += game

        game += 1

    return sum


def part_2():
    input_arr = get_all_strings_by_lines('2.txt')

    sum = 0
    for val in input_arr:
        sets = val.split('; ')
        min_config = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for s in sets:
            pulls = s.split(', ')
            for pull in pulls:
                count_s, color = pull.split(' ')
                count = int(count_s)
                # log(f'Game {game}: {s}: {pull}: {count} {color}')
                if count > min_config[color]:
                    min_config[color] = count

        # Find the power and add it to the sum
        sum += min_config['red'] * min_config['green'] * min_config['blue']


    return sum