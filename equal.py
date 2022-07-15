# https://www.hackerrank.com/challenges/equal/problem?isFullScreen=true

def g(diff):
    ans = {0:0, 1:1, 2:1, 3:2, 4:2}
    return diff // 5 + ans[diff % 5]

def f(chocolates, goal):
    return sum(g(chocolate-goal) for chocolate in chocolates)

def equal(arr):
    # Write your code here
    min_chocolate = min(arr)
    return min(f(arr, min_chocolate - dc) for dc in range(4))
