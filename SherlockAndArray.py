# https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true

def balancedSums(arr):
    # Write your code here
    total_sum = sum(arr)
    cummulative = 0
    response = 'NO'
    
    for item in arr:
        if total_sum - cummulative == cummulative + item:
            response = 'YES'
            break
        cummulative += item
    return response
