# https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n - 1)
    
def extraLongFactorials(n):
    # Write your code here
    print(factorial(n))
