# ruby implementation of Binary search algorithm

def binary_search(array, key, low=0, high=array.size-1)
    return -1 if low > high
   
    mid = (low + high)/2
    return mid if array[mid] == key
   
    if array[mid] > key
        high = mid - 1
    else
        low = mid + 1
    end
   
    binary_search(array, key, low, high)
end

array = (1_000..10_000_000).to_a
p binary_search(array, 1_001)
