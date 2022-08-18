# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem?isFullScreen=true

from math import factorial, exp

miu = float(input())
x = int(input())
poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)
print("%.3f" %poisson_prob)
