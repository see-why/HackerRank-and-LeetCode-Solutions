# https://www.hackerrank.com/challenges/largest-permutation/problem?isFullScreen=true

def largestPermutation(k, arr):
    # Write your code here
        i, swaps = 0, 0        
        index = len(arr)
        dict = {}
        
        for counter in range(len(arr)):
            dict[arr[counter]] = counter  
            
        while swaps < k and i<index:
            x = index - i
            y = arr[i]
            
            if y != x:
                arr[dict[x]] = y
                arr[i] = x
                dict[x],dict[y] = dict[y],dict[x]
                swaps += 1
            
            i += 1
        
        return arr
