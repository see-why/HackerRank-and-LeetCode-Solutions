# https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true

def gridSearch(G, P):
    # Write your code here
    def check(i,j):
        for x in range(r):
            if P[x] != G[i+x][j:j+c]:
                return False
        return True
    
    result = "NO"
        
    for i in range(R):
        for j in range(C):
            print(G[i][j])
            if G[i][j] == P[0][0]:
                if check(i,j):
                    return "YES"
                
    return result
