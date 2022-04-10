# https://www.hackerrank.com/challenges/misere-nim-1/problem?isFullScreen=true

def misereNim(s):
    # Write your code here
    result = 'First'
    x = reduce(lambda x, y: x ^ y,s)

    if len(set(s))==1 and 1 in s:
        if x:
            result = 'Second'
    else:
        if x == False:
            result = 'Second'

    return result
        
