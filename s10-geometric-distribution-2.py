https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem?isFullScreen=true


p=1/3

def geomprob(k,p):
    return p*(1-p)**(k-1)

print("{0:.3f}".format(sum([geomprob(k,p) for k in range(1,6)])))
