# https://www.hackerrank.com/challenges/nim-game-1/problem?isFullScreen=true 

def nimGame(pile):
    # Write your code here
    result = 'First'
    if reduce(lambda x, y: x ^ y, pile) == 0:
        result = 'Second'
            
    return result
