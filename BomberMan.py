# https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true

def bomberMan(n, grid):
    # Write your code here
    def printList(array):
        for i in range(len(array)):
            array[i] = ''.join(map(str,array[i]))
        return array
    
    def bomb(previous_grid, r,c):
        complete_state = [['O' for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if previous_grid[i][j] == 'O':
                    complete_state[i][j] = '.'
                    if i+1<r:
                        complete_state[i+1][j] = '.'
                    if i>0:
                        complete_state[i-1][j] = '.'
                    if j+1<c:
                        complete_state[i][j+1] = '.'
                    if j>0:
                        complete_state[i][j-1] = '.'
        return complete_state
        
    next_state = bomb(grid, r,c)
    last_state = bomb(next_state, r,c)
    
    if n == 1:
        return printList(grid)
    elif n%2 == 0:
        return printList(['O'*c for i in range(r)])
    elif (n-3) % 4 ==0:
        return printList(next_state)
    else:
        return printList(last_state)
