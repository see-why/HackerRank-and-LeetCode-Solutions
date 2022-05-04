# https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true

def countSort(arr):
    # Write your code here
    sort=[""]*100
    for a0 in range(n):        
        x, s = arr[a0][0], arr[a0][1]
        x, s = [int(x), str(s)]
        if a0<n//2:
            sort[x]+="- "
        else:
            sort[x]+=s+" "
    print("".join(i for i in sort))
