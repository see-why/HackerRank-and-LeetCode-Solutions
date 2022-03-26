# https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true

def missingNumbers(arr, brr):
    # Write your code here
    response = []
    a = collections.Counter(arr)
    b = collections.Counter(brr)
    
    for number in b.keys():
        if number in a.keys():
            diff_frequency = b[number] - a[number]
            if diff_frequency > 0:
                response.append(number)
        else:
            response.append(number)

    response.sort()
    return response
