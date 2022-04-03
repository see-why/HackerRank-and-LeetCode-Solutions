# https://www.hackerrank.com/challenges/poker-nim-1/problem?isFullScreen=true

def pokerNim(k, c):
    # Write your code here
    score = 0
    for ctemp in c: 
        score ^= ctemp
        
    if score==0: 
        return "Second"
    else:
        return "First"
