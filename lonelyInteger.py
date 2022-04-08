# https://www.hackerrank.com/challenges/lonely-integer/problem?isFullScreen=true

def lonelyinteger(a):
    # Write your code here
    dict = collections.Counter(a) 
    result = [item for item in dict.keys() if dict[item] == 1]
    return result.pop()
