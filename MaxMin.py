# https://www.hackerrank.com/challenges/angry-children/problem?isFullScreen=true

def maxMin(k, arr):
    # Write your code here
    k-=1
    arr.sort()
    return min(arr[i+k]-arr[i] for i in range(len(arr)-k))
