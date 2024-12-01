from lib.helpers import log, get_strings_by_lines, TEST_MODE


# D(wait) = (t - wait) * wait = wait * t - wait ^ 2
distance = lambda t, wait: wait * t - (wait ** 2)

def count_solutions(time, min_dist):
    count = 0
    for wait in range(1, time):
        if distance(time, wait) > min_dist:
            count += 1
    
    return count

def first_solution(time, min_dist):
    for wait in range(1, time):
        if distance(time, wait) > min_dist:
            return wait

def last_solution(time, min_dist):
    for wait in range(time, 1, -1):
        if distance(time, wait) > min_dist:
            return wait
    

def part_1():
    input_arr = get_strings_by_lines('6.txt')
    times = [int(t) for t in input_arr[0].split(' ') if t != '']
    dist = [int(d) for d in input_arr[1].split(' ') if d != '']

    log(times)
    log(dist)

    product = 1
    for i in range(len(times)):
        log(f"Time: {times[i]}, Distance: {dist[i]}")
        solutions = count_solutions(times[i], dist[i])
        log(f"Found: {solutions} solutions\n")
        product *= solutions

    return product

def part_2():
    times = [71530] if TEST_MODE else [49787980]
    distance = [940200] if TEST_MODE else [298118510661181]

    first = first_solution(times[0], distance[0])
    log(f"First solution: {first}")
    last = last_solution(times[0], distance[0])
    log(f"Last solution: {last}")
    return last - first + 1