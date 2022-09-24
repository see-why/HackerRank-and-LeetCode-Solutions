# smallest subarray with a given sum

# brute force
def smallest_subarray(array, k)
    sum = 0
    min_count = Float::INFINITY
    for i in (0..array.size-1)
        counter = 1
        sum = array[i]
        min_count = counter if sum >= k
        for j in (i+1..array.size-1)
            if sum >= k
                min_count = counter if counter < min_count
                break
            end
            sum += array[j]
            counter += 1
        end
    end
    min_count == Float::INFINITY ? sum : min_count
end

# sliding pattern
def smallest_subarray_sliding(array, k)
    min_count, sum, start = Float::INFINITY, 0, 0
    for windows_end in (0..array.size-1)
        sum += array[windows_end]
       
        while sum >= k
            min_count = [ min_count, windows_end - start+1 ].min { |a, b| a<=>b}
            sum -= array[start]
            start += 1
        end
    end
    min_count == Float::INFINITY ? 0 : min_count
end
