# https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true

def icecreamParlor(m, arr):
    # Write your code here
    index = []

    for counter,item in enumerate(arr):
        diff = m - item
        if diff in arr:
            index_of_diff = arr.index(diff)
            
            if diff == item:
                if diff in arr[arr.index(diff)+1:]:
                    index_of_diff = arr[arr.index(diff)+1:].index(diff)
                    index_of_diff = index_of_diff+1+counter
                else:
                    index_of_diff = 0
                    
            if index_of_diff != 0:
                index.append(counter+1)
                index.append(index_of_diff+1)
                break
        
    return index
