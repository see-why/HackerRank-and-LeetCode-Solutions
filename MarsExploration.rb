# https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true

def marsExploration(s)
    # Write your code here
    array = s.chars
    i = 0
    counter = 0
    array.each do 
        counter += 1 if array[i] != "S"
        counter += 1 if array[i+1] != "O"
        counter += 1 if array[i+2] != "S"
        i += 3
        break if i >= array.size - 1
    end
    
    counter
end
