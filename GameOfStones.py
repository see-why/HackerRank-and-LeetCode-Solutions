# https://www.hackerrank.com/challenges/game-of-stones-1/problem?isFullScreen=true

def gameOfStones(n):
    # Write your code here
    if n%7 == 1 or n%7 == 0:
        return "Second"
    else:
        return "First"
