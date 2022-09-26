
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
