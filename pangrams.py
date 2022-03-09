# https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true

def pangrams(s):
    # Write your code here
    alphabet = set(string.ascii_lowercase)
    return "pangram" if set(s.lower()) >= alphabet else "not pangram"
  
