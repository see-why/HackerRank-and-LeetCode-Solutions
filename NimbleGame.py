# https://www.hackerrank.com/challenges/nimble-game-1/problem?isFullScreen=true

def nimbleGame(s):
    # Write your code here
    xor_sum = 0
    for n,pile in enumerate(s):
        if pile % 2 == 1:
            xor_sum = xor_sum ^ n
    if xor_sum == 0:
        return 'Second'
    else:
        return 'First'
