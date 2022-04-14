# https://www.hackerrank.com/challenges/two-arrays/problem?isFullScreen=true

def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    result = [a+b for a,b in zip(A,B) if a+b >= k]
    
    return 'YES' if len(result) == len(A) else 'NO'
