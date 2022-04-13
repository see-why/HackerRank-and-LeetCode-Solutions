# https://www.hackerrank.com/challenges/sum-vs-xor/problem?isFullScreen=true

def sumXor(n):
    # Write your code here
    counter = 0
    binary_string = '{0:b}'.format(n)
    print(binary_string)
    for bit in binary_string:
        if bit == '0':
            counter += 1
    if n == 0:
        counter = 0
    return 2**counter
