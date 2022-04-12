# https://www.hackerrank.com/challenges/largest-permutation/problem?isFullScreen=true

def largestPermutation(k, arr):
    # Write your code here
    if k >= len(arr) - 1:
        return sorted(arr, reverse = True)
    
    else:
        sorted_array = sorted(arr)
        i, swaps = 0, 0
        
        while swaps < k:
            x = sorted_array.pop()
            
            if arr[i] != x:
                arr[arr.index(x)] = arr[i]
                arr[i] = x
                swaps += 1
            
            i += 1
        
        return arr
