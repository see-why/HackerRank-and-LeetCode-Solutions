# https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true

def surfaceArea(A):
    # Write your code here
    ans = 2*H*W
    for i in range(H):
        for j in range(W):
            # top
            if i == 0:
                ans += A[i][j]
            
            # left
            if j == 0:
                ans += A[i][j]
            
            # right
            if j == W-1:
                ans += A[i][j]
            else:
                ans += abs(A[i][j]-A[i][j+1])
            
            # bottom
            if i == H-1:
                ans += A[i][j]
            else:
                ans += abs(A[i][j]-A[i+1][j])
    return ans
