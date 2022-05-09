# https://www.hackerrank.com/challenges/maximum-palindromes/problem?isFullScreen=true


def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    count_s = Counter(s[l-1:r])
    print(count_s)
    odd_number = 0

    sum_of_even_numbers_factorial = 1
    sum_of_even_number = 0
    for i in count_s:
        sum_of_even_numbers_factorial *= factorial(count_s[i]//2)
        sum_of_even_number += count_s[i]//2
        if count_s[i]%2 == 1:
            odd_number += 1

    ans = 0
    if odd_number == 0:
        ans = factorial(sum_of_even_number) // sum_of_even_numbers_factorial
    else:
        ans = factorial(sum_of_even_number) // sum_of_even_numbers_factorial * odd_number

    return (ans % (10**9+7))
