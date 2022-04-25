# https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true

def absolutePermutation(n, k):
    # Write your code here
    if k == 0: return range(1,1+n)
    if n%(2*k): return [-1]
    base = range(k+1,2*k+1) + range(1,1+k)
    ans = []
    Q = n/(2*k)
    for q in xrange( Q ):
        for i in base:
            ans.append( q*2*k + i )
    return ans
