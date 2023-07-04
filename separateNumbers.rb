# https://www.hackerrank.com/challenges/three-month-preparation-kit-separate-the-numbers/problem

def separateNumbers(s)
    # Write your code here
    start_str_arr = []

    0.upto (s.size/2) do |ind|
        start_str = s[..ind]
        build_str = ''
        num = start_str.to_i
       
        next if start_str.size == s.size

        while build_str.size < s.size
            build_str += (num).to_s
            num += 1
        end

        start_str_arr << start_str if build_str === s
    end
    start_str_arr.sort
   
    result = start_str_arr.empty? ? 'NO' : "YES #{start_str_arr[0]}"
    puts result
end
