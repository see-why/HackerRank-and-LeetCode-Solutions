# https://www.hackerrank.com/challenges/clique/problem?h_r=profile

def clique(n, m):
    # Write your code here
    low = 1
    high = n+1
    ret = -1
    
    while low + 1 < high:
        mid = (low + high) // 2
        
        if int(get_calc(mid,n)) < m:
            low = mid
        else:
            high = mid
    return high

def get_calc(m, n):
    g1 = n % m
    g2 = m - g1
    sz1 = n // m + 1
    sz2 = n // m
    
    return g1 * sz1 * g2 * sz2 + g1 * (g1 - 1) * sz1 * sz1 / 2 + g2 * (g2 - 1) * sz2 * sz2 / 2
