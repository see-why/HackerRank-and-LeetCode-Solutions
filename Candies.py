# https://www.hackerrank.com/challenges/candies/problem?isFullScreen=true

def candies(n, arr):
    # Write your code here
    candies_array = [1]*n
    for i in range(n-1):
        if arr[i+1]>arr[i]:
            candies_array[i+1] = candies_array[i]+1
    for i in range(n-1,0,-1):
        if arr[i-1]>arr[i] and candies_array[i-1]<=candies_array[i]:
            candies_array[i-1] = candies_array[i]+1
    return sum(candies_array)
