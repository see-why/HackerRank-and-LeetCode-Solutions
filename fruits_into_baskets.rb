# grokking the coding interview: fruits into basket

def  fruits_into_baskets(fruits)
    maxLength = 0
    fruitsFrequency = {}
    windows_start = 0
   
    for window_end in 0..(fruits.size)
        current_fruit = fruits[window_end]
        if fruitsFrequency[current_fruit]
         fruitsFrequency[current_fruit] += 1
        else
         fruitsFrequency[current_fruit] = 1
        end
         
        while fruitsFrequency.size > 2 do
            left_fruit = fruits[windows_start]
            fruitsFrequency[left_fruit] -= 1
            fruitsFrequency.delete(left_fruit) if fruitsFrequency[left_fruit].zero?
            windows_start += 1
           
        end
       
       
        maxLength = [maxLength, (window_end-windows_start+1)].max
    end
   
    maxLength
end
