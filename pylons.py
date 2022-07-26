# https://www.hackerrank.com/challenges/pylons/problem?isFullScreen=true

def voisins(i):
    return range(min(n-1, i+k-1), max(-1, i-k), -1)

def pylons(k, arr):
    # Write your code here
    count = 0
    past_fourni = 0
    while past_fourni < n:
        for i in voisins(past_fourni):
            if arr[i]:
                past_fourni = i + k
                count += 1
                break
            else:
                count = -1
                break                
    return(count)
