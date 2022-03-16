# https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true

def alternatingCharacters(s):
    # Write your code here
        result=0
        if 'A' not in s or 'B' not in s:
            result = len(s)-1
            return result
        i=0
        while i<(len(s)-1):
            if s[i+1]==s[i]:
                result+=1
            i+=1
        return result
