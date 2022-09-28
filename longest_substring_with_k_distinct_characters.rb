
# longest substring with K distinct characters

def distinct_substring string, k
    windows_start, counter, size = 0, 0, string.size-1
    substring = []
   
    for windows_start in (0..size)
        for windows_end in (windows_start..size)
            substring << string[windows_end]
           
            if no_of_distinct_characters(substring) == k
                counter = substring.size > counter ? substring.size : counter
            end
        end
        substring.clear
    end
   
    counter
end
           
def no_of_distinct_characters string
    string.to_a.uniq.size
end


p distinct_substring("araaci", 2)
p distinct_substring("araaci", 1)
p distinct_substring("cbbebi", 3)

def distinct_substring_sliding string, k
    windows_start, max_length, size = 0, 0, string.size-1
    char_hash = {}
   
    for windows_end in (0..size)
        right_char = string[windows_end]
        char_hash[right_char] = char_hash[right_char] ? char_hash[right_char] += 1 : 1
       
        while char_hash.size > k
            left_char = string[windows_start]
            char_hash[left_char] -= 1
           
            if char_hash[left_char] == 0
                char_hash.delete(left_char)
            end
           
            windows_start += 1
            max_length = [max_length, windows_end-windows_start+1].max
        end
    end
   
    max_length
end

p distinct_substring_sliding("araaci", 2)
p distinct_substring_sliding("araaci", 1)
p distinct_substring_sliding("cbbebi", 3)
