def insertion_sort array
    final = [array[0]]
    array.delete_at(0)
    
    array.each do |i|
        final_index = 0
        while final_index < final.length
            if i <= final[final_index]
                final.insert(final_index, i)
                break
            elsif final_index == final.length - 1
                final.insert(final_index + 1, i)
            end
            final_index += 1
        end
    end
    final
end
