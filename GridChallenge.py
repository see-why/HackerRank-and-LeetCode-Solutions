# https://www.hackerrank.com/challenges/grid-challenge/problem

def gridChallenge(grid):
    # Write your code here
    count = 0
    for i in range(len(grid)):
        item = sorted(grid[i])
        item = "".join(item)
        grid[i] = item
        
    for j in range(len(grid[0])):
        for i in range(len(grid)-1):
            if grid[i][j] > grid[i+1][j]:
                return "NO"
        
    return "YES"
