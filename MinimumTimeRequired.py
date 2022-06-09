# https://www.hackerrank.com/challenges/minimum-time-required/problem?isFullScreen=true

def minTime(machines, goal):
    machines, count = sorted(machines), len(machines)
    min_day = math.ceil(goal / count) * machines[0]
    max_day = math.ceil(goal / count) * machines[-1]

    while min_day < max_day:
        day = (max_day + min_day) // 2
        day_sum = sum(day // m for m in machines)

        if day_sum >= goal:
            max_day = day
        else:
            min_day = day + 1

    return min_day
