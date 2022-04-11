# https://www.hackerrank.com/challenges/maximizing-xor/problem?isFullScreen=true

def maximizingXor(l, r):
    # Write your code here
    result = 0
    
    for i in range(l, r+1):
        for j in range(i, r+1):
            value = i^j
            result = value if value > result else result
    
    return result
