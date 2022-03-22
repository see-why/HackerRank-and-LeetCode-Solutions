# https://www.hackerrank.com/challenges/anagram/problem?isFullScreen=true

def anagram(s):
    # Write your code here
    if len(s)%2: return -1
    l = len(s)//2
    a = collections.Counter(s[:l])
    b = collections.Counter(s[l:])
    return l-sum((a & b).values())
