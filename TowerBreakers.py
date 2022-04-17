# https://www.hackerrank.com/challenges/tower-breakers-1/problem?isFullScreen=true

def towerBreakers(n, m):
    # Write your code here
    result = 1
    if m == 1: 
        result = 2
    else:
        if n % 2 != 1:
            result = 2

    return result
