#  https://www.hackerrank.com/challenges/flipping-bits/problem?isFullScreen=true

def flippingBits(n):
    # Write your code here
    result = 0
    for i in range(31,-1,-1):
        if n//(2**i) == 1:
            n = n - 2**i
            x = 0
        else:
            x = 1
        result += 2**i * x

    return result
