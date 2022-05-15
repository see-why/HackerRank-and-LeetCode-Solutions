# https://www.hackerrank.com/challenges/minimum-loss/problem?isFullScreen=true

def minimumLoss(price):
    # Write your code here 
    dict = { price[i]: i for i in range(n) }    
    price = sorted(price)
    result = 10 ** 6
    
    for ind,val in enumerate(price):
        index = min(ind+1,len(price)-1)
        if dict[val] > dict[price[index]]:            
            result = min(result, price[index]-val)
    
    return result
