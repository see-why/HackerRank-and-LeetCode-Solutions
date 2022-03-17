# https://www.hackerrank.com/challenges/countingsort2/problem?isFullScreen=true

def beautifulBinaryString(b):
    # Write your code here
    if '010' not in b:
        return 0
    else:
        return b.count('010')
      
     
