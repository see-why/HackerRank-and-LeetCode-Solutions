# https://www.hackerrank.com/challenges/triple-sum/problem?isFullScreen=true

def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    ai = 0
    bi = 0
    ci = 0
    
    ans = 0
    
    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        
        ans += ai * ci
        bi += 1
    
    return ans
