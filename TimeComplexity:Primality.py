# https://www.hackerrank.com/challenges/ctci-big-o/problem?isFullScreen=true

def primality(n):
    # Write your code here
    if(n>1):
        for i in range(2,int(sqrt(n))):
            if(n%i==0):
                return ("Not prime")
            
    if(n<=1):
        return ("Not prime")
    else:
        return ("Prime")
