# sliding window pattern, ruby implementation

def find_average_sub_arrays_sliding(array, k)
    result = []
   
    window_start, sum = 0, 0.0
    for window_end in (0..array.size-1)
        sum += array[window_end]
        if window_end >= k-1
            avg = sum/k
            result << avg
            sum -= array[window_start]
            window_start += 1
        end
    end
    p result
end
