# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem?isFullScreen=true

from bisect import bisect,insort

def maximumSum(a, m):
    # Write your code here
    cumulative_sums = []
    sum_so_far = 0
    max_sum = 0
    
    for i in range(n):
        sum_so_far = (sum_so_far + a[i]) % m        
        pos = bisect(cumulative_sums, sum_so_far)
        d = 0 if pos == i else cumulative_sums[pos]
        max_sum = max(max_sum, (sum_so_far + m - d) % m)
        insort(cumulative_sums, sum_so_far)
    
    return (max_sum)
