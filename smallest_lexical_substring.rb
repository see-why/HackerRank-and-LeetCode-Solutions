def smallest_lexical_substring str
    str_arr = str.split('')
    char_array = str_arr.uniq
    substrings_array = []
   
    char_array.each_with_index do |item, ind|
        a = item
        next_index = ind + 1
        until next_index == char_array.size
          b = char_array[next_index]
          substring = str_arr.map do |item|
              if item == a
                b
              elsif item == b
                a
              else
                item
              end
          end
          substrings_array << substring.join('')
          next_index += 1
        end
    end
   
    substrings_array.sort.first
end

pp smallest_lexical_substring "abbccdde"
pp smallest_lexical_substring "dcab"
pp smallest_lexical_substring "zyzx"
pp smallest_lexical_substring "cba"
pp smallest_lexical_substring "aabbccdd"
pp smallest_lexical_substring "aabcc"
