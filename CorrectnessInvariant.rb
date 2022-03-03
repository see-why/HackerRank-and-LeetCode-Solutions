# https://www.hackerrank.com/challenges/correctness-invariant/problem?isFullScreen=true

def  insertionSort(ar)
    i = 1
    while (i < ar.length)
        if (i > 0 && ar[i] < ar[i - 1])
            value = ar[i]
            j = i-1
            while (j >= 0 && value < ar[j])
                value = ar[j+1] 
                ar[j+1] = ar[j]
                ar[j] = value
                j -= 1
            end
        end
        i += 1
    end
    puts ar.join(" ")
end
