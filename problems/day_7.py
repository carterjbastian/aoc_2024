from lib.helpers import log, get_strings_by_lines
import functools
 
ordered_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
def cmp(a_pair, b_pair):
    a = a_pair[0]
    b = b_pair[0]
    uniques_a = len(set(a))
    uniques_b = len(set(b))

    if uniques_a > uniques_b:
        return 1
    elif uniques_a < uniques_b:
        return -1
    
    # Tiebreaker 1: 4 a kind beats full house, 3 of a kind beats 2 pair
    freq_dict_a = {}
    freq_dict_b = {}
    for idx in range(len(a)):
        freq_dict_a[a[idx]] = freq_dict_a.get(a[idx], 0) + 1
        freq_dict_b[b[idx]] = freq_dict_b.get(b[idx], 0) + 1
    max_a = max(freq_dict_a.values())
    max_b = max(freq_dict_b.values())
    if max_a < max_b:
        return 1
    elif max_a > max_b:
        return -1

    # Tiebreaker 2: check each card
    for idx in range(len(a)):
        if ordered_cards.index(a[idx]) > ordered_cards.index(b[idx]):
            return 1
        elif ordered_cards.index(a[idx]) < ordered_cards.index(b[idx]):
            return -1

    return 0

def part_1():
    txt = get_strings_by_lines('7.txt')

    hands = []
    for line in txt:
        hand, bid = line.split(' ')
        hands.append((hand, int(bid)))
    log(hands)


    hands.sort(key=functools.cmp_to_key(cmp), reverse=True)
    log(hands)
    multiplier = 1
    score = 0
    for hand in hands:
        score += hand[1] * multiplier
        multiplier += 1


    return score

ordered_cards_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def cmp_2(a_pair, b_pair):
    a = a_pair[0]
    b = b_pair[0]

    freq_dict_a = {}
    freq_dict_b = {}
    for idx in range(len(a)):
        freq_dict_a[a[idx]] = freq_dict_a.get(a[idx], 0) + 1
        freq_dict_b[b[idx]] = freq_dict_b.get(b[idx], 0) + 1
    
    jokers_a = freq_dict_a.get('J', 0)
    jokers_b = freq_dict_b.get('J', 0)

    uniques_a = len(set(a)) - 1 if jokers_a > 0 else len(set(a))
    uniques_b = len(set(b)) - 1 if jokers_b > 0 else len(set(b))
    uniques_a = max(uniques_a, 2)
    uniques_b = max(uniques_b, 2)

    if uniques_a > uniques_b:
        return 1
    elif uniques_a < uniques_b:
        return -1
    
    # Tiebreaker 1: 4 a kind beats full house, 3 of a kind beats 2 pair
    if jokers_a > 0:
        del freq_dict_a['J']
    if jokers_b > 0:
        del freq_dict_b['J']

    max_a = max(max(freq_dict_a.values()) + jokers_a, 4) if a != 'JJJJJ' else 4
    max_b = max(max(freq_dict_b.values()) + jokers_b, 4) if b != 'JJJJJ' else 4
    if max_a < max_b:
        return 1
    elif max_a > max_b:
        return -1

    # Tiebreaker 2: check each card
    for idx in range(len(a)):
        if ordered_cards_2.index(a[idx]) > ordered_cards_2.index(b[idx]):
            return 1
        elif ordered_cards_2.index(a[idx]) < ordered_cards_2.index(b[idx]):
            return -1

    return 0

def part_2():
    txt = get_strings_by_lines('7.txt')

    hands = []
    for line in txt:
        hand, bid = line.split(' ')
        hands.append((hand, int(bid)))
    log(hands)


    hands.sort(key=functools.cmp_to_key(cmp_2), reverse=True)
    log(hands)
    multiplier = 1
    score = 0
    for hand in hands:
        score += hand[1] * multiplier
        multiplier += 1

    return score