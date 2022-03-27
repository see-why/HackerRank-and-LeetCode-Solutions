# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    diff_array = []
    for i in range(len(arr)-1):
        diff_array.append(abs(arr[i]-arr[i+1]))
    return min(diff_array)
