# https://www.hackerrank.com/challenges/s10-standard-deviation/problem?isFullScreen=true


from statistics import mean

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    avg = mean(arr)
    sum = 0
    
    for i in range(n):
        diff = arr[i] - avg
        sum += diff * diff
        
    std = math.sqrt(sum/n)
    print (round(std, 1))
