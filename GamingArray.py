# https://www.hackerrank.com/challenges/an-interesting-game-1/problem?isFullScreen=true


def gamingArray(arr):
    # Write your code here
    maxes = []
    cur_max = -float("inf")
    for i, num in enumerate(arr):
        if num > cur_max:
            cur_max = num
            maxes.append(i)
    if len(maxes) % 2 == 0:
        return("ANDY")
    else:
        return("BOB")
