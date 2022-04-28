# https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true

def larrysArray(A):
    # Write your code here
    return "NO" if sum((1 for i in range(len(A)) for j in range(i+1, len(A)) if A[i] > A[j] ))%2 else "YES"
