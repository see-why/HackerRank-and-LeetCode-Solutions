# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem?isFullScreen=true

def geometric_distributon(n, p):
    return ((1-p)**(n-1))*p

a, b = list(map(int, input().split()))
n = int(input())
print('{:.3f}'.format(geometric_distributon(n, a/b)))
