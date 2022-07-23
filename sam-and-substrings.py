# https://www.hackerrank.com/challenges/sam-and-substrings/problem?isFullScreen=true

def substrings(n):
    s = 0
    prev_sum = 0
    
    for i, d in enumerate(n):
        s_ = prev_sum * 10 + (i + 1) * int(d)
        s += s_
        prev_sum = s_
    return s % (10 ** 9 + 7)
