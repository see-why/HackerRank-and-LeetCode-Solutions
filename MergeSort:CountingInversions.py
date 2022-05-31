# https://www.hackerrank.com/challenges/ctci-merge-sort/problem?isFullScreen=true


def countInversions(arr):
    # Write your code here
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
 
    return inv_count
