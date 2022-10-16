# counting family login pairs, where pairs are a character transform each from the other e.g. "abc" and "bcd"

def family_pairs(logins)
    family_pairs_counter = 0
    logins.map do |item|
        possible_pairs = [""]
        item.each_char do |letter|
            code = letter.ord
            possible_pairs[0] += code == 122 ? "a" : (code + 1).chr
        end

        family_pairs_counter += logins.count(possible_pairs[0])
    end

    family_pairs_counter
end

puts family_pairs ['ab', 'bc', 'zz', 'aa', 'bb', 'cc', 'cc', 'cc', 'aa'] //8
