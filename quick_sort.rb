# ruby implementation of the quick sort algorithm

# extending the Array class
class Array
    def quick_sort
        return [] if empty?
        pivot = delete_at(rand(size))
        left, right = partition(&pivot.method(:>))
        return *left.quick_sort, pivot, *right.quick_sort
    end
end

array = (1..500).to_a.shuffle
p array.quick_sort

# method that takes in an array
def quick_sort array
    return [] if array.empty?
    pivot = array.delete_at(rand(array.size))
    left, right = array.partition { |num| num < pivot }
    return [quick_sort(left), pivot, quick_sort(right)].flatten
end


array = (1..500).to_a.shuffle
p quick_sort array
