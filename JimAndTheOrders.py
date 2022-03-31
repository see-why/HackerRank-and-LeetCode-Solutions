# https://www.hackerrank.com/challenges/jim-and-the-orders/problem?isFullScreen=true

def jimOrders(orders):
    # Write your code here
    dict = {}
        
    for i in range(len(orders)):
        sum = orders[i][0] + orders[i][1]
        dict[i+1] = sum
    
    # returns an array
    dict = sorted(dict.items(), key = lambda kv:(kv[1], kv[0]))
             
    return [item[0] for item in dict]
