from lib.helpers import log, get_input

def convert(val, conversion_rules):
    for rule in conversion_rules:
        start_dest, start_source, range_len = rule
        if start_source <= val < start_source + range_len:
            return start_dest + (val - start_source)
    
    return val

def invert(val, conversion_rules):
    for rule in conversion_rules:
        start_dest, start_source, range_len = rule
        if start_dest <= val < start_dest + range_len:
            return start_source + (val - start_dest)
    
    return val

def part_1():
    input_arr = get_input('5.txt')
    substrings = input_arr.split('\n\n')
    seed_s = substrings[0]
    conversion_strings = substrings[1:]
    conversions = []
    seed = [int(val) for val in seed_s.split(' ') if val != '']
    log(seed)
    log(conversion_strings[-1])

    for conv_s in conversion_strings:
        rules = []
        for rule_s in conv_s.split('\n'):
            rules.append(tuple([int(val) for val in rule_s.split(' ') if val != '']))
        
        conversions.append(rules)

    log(conversions)

    min = float('inf')
    for seed_val in seed:
        log('\n\nSeed: ' + str(seed_val))
        cur = seed_val
        for conversion in conversions:
            cur = convert(cur, conversion)
            log(cur)
        
        if (cur < min):
            min = cur

    return min

def part_2():
    input_arr = get_input('5.txt')
    substrings = input_arr.split('\n\n')
    seed_s = substrings[0]
    conversion_strings = substrings[1:]
    conversions = []
    seeds = [int(val) for val in seed_s.split(' ') if val != '']

    for conv_s in conversion_strings:
        rules = []
        for rule_s in conv_s.split('\n'):
            rules.append(tuple([int(val) for val in rule_s.split(' ') if val != '']))
        
        conversions.append(rules)

    conversions.reverse()
    location = 0
    while True:
        # Upper bound found with some manual binary searching
        if location == 80000000:
            return 0
        if location % 1000000 == 0:
            log(f'Checking Location: {location}')

        cur = location
        for conversion in conversions:
            cur = invert(cur, conversion)
        
        for idx in range(int(len(seeds) / 2)):
            # Work backwards from the location
            start = seeds[idx * 2]
            range_len = seeds[(idx * 2) + 1]
            if start <= cur < start + range_len:
                return location
        # Change this to 100 to scan for the range
        location += 1