# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?isFullScreen=true

var = [0] *40


def fibonacci(n):
    if n <= 1:
        return n
    if var[n] == 0:
        var[n] = fibonacci(n-1) + fibonacci(n-2)
    return var[n]

n = int(input())
print(fibonacci(n))
