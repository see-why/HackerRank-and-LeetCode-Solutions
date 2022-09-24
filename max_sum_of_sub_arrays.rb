# find max sum of sub arrays of size k

def max_of_sub_arrays(array, k)
    max = 0.0
   
    window_start, sum = 0, 0.0
    for window_end in (0..array.size-1)
        sum += array[window_end]
        if window_end >= k-1
            max = sum if sum >= max
            sum -= array[window_start]
            window_start += 1
        end
    end
   
    max
end

array = [2,1,5,1,3,2]
sums = find_average_sub_arrays_sliding(array, 3)
p sums
sums = sums.map { |num| num *= 3 }
p sums
p max_of_sub_arrays array, 3

array, k = [2,3,4,1,5], 2
sums = find_average_sub_arrays_sliding(array, k)
p sums
sums = sums.map { |num| num *= k }
p sums
p max_of_sub_arrays array, k
