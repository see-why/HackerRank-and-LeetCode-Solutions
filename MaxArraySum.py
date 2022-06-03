# https://www.hackerrank.com/challenges/max-array-sum/problem?isFullScreen=true

def maxSubsetSum(arr):
    if arr == None or len(arr) == 0:
        return 0

    n = len(arr)
    if n == 1:
        return arr[0]


    maximum_sum = max(arr[0], arr[1])
    arr[1] = maximum_sum;
    for i in range(2,n):
        maximum_sum = max(arr[i-2] + arr[i], maximum_sum)
        maximum_sum = max(arr[i], maximum_sum)
        arr[i] = maximum_sum; 

    return maximum_sum
