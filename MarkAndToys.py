#https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true

def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    count = 0
    sum = 0
    i = 0
    while sum < k:
        sum += prices[i]
        i += 1
        count += 1
    return count - 1
