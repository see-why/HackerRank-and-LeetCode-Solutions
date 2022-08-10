# https://www.hackerrank.com/challenges/s10-quartiles/problem?isFullScreen=true

from statistics import median

def quartiles(arr):
    arr = sorted(arr)
    
    q1 = int(median(arr[:n//2]))
    q2 = int(median(arr))
    q3 = int(median(arr[((n+1)//2):]))
    return [q1, q2, q3]
