# https://www.hackerrank.com/challenges/s10-interquartile-range/problem?isFullScreen=true


from statistics import median

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    s = []
    for i in range(n):
        s += [values[i]] * freqs[i]
    N = sum(freqs)
    
    arr = sorted(s)
    
    q1 = int(median(arr[:N//2]))
    q2 = int(median(arr))
    q3 = int(median(arr[((N+1)//2):]))
    
    print (round(float(q3-q1), 1))
