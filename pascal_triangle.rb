'''
pascal_triangle(9) prints:

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]

'''

import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))
    
def print_row(n):
    array = [1]
    if n == 2:
        array.append(1)
    elif n > 2:
        array += compute_coefficients(n-1) + [1]
    print(array)
    
def compute_coefficients(n):
    array = []
    stop_index = math.ceil(n/2)+1
    for i in range(1,stop_index):
        array.append(combination(n, i))
    
    reversed = array[::-1]
    
    result = array + reversed[1:] if n %2 == 0 else array + reversed[2:]
    return result
    
def pascal_triangle(n):
    for i in range(1,n+1):
        print_row(i)
        

