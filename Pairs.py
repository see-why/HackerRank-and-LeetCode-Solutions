# https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true

def pairs(k, arr):
    # Write your code here    
    count = 0    
    uniques_values = set(arr)
    for ind,val in enumerate(arr):        
        if val+k in uniques_values:
           count+=1
        
    return count
