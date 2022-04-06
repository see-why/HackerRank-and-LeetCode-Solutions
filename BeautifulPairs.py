# https://www.hackerrank.com/challenges/beautiful-pairs/problem?isFullScreen=true

def beautifulPairs(A, B):
    # Write your code here
    count = 0
    for i in range(n):
        for j in range (n):
            if A[i] == B[j] and A[i] > 0:
                count += 1
                A[i] = 0
                B[j] = 0
            
    if count < n:
        count += 1
    else:
        count -= 1  
        
    return count
