# https://www.hackerrank.com/challenges/s10-weighted-mean/problem?isFullScreen=true


def weightedMean(X, W):
    # Write your code here
    size = len(X)
    weightedSum = 0
    sum = 0
    
    for x in range(size):
        weightedSum += X[x] * W[x]
        sum += W[x]
        
    print('{0:3.1f}'.format(weightedSum/sum))
        
