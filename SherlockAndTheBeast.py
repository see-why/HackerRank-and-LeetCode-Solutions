# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem?isFullScreen=true

def decentNumber(n):
    # Write your code here
    a, b = divmod(n,3)
    print("{a}:{b}").format(a=a, b=b)
    while b%5:
        b+=3
        a-=1
    if a>-1:
        print("5"*a*3+"3"*b)
    else:
        print("-1")
