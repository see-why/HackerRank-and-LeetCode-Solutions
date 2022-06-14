# https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_r=profile

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    a,b,c,d = startX, startY, goalX, goalY
    N = n

    moves = [[[a,b]]]
    visited = [[False for i in range(N)] for j in range(N)]
    visited[a][b] = True

    while [c,d] not in moves[-1]:
        nxt = []

        for m in moves[-1]:
            i = m[0]+1
            j = m[1]
            while i < N and grid[i][j] != 'X':
                if not visited[i][j]:
                    nxt.append([i,j])
                    visited[i][j] = True
                i += 1

            i = m[0]-1
            j = m[1]
            while i >= 0 and grid[i][j] != 'X':
                if not visited[i][j]:
                    nxt.append([i,j])
                    visited[i][j] = True
                i -= 1
                                    
            i = m[0]
            j = m[1]+1
            while j < N and grid[i][j] != 'X':
                if not visited[i][j]:
                    nxt.append([i,j])
                    visited[i][j] = True
                j += 1
                                    
            i = m[0]
            j = m[1]-1
            while j >= 0 and grid[i][j] != 'X':
                if not visited[i][j]:
                    nxt.append([i,j])
                    visited[i][j] = True
                j -= 1              
        moves.append(nxt)                           
                
    return(len(moves)-1)
