# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem?isFullScreen=true

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks = sorted(sticks)
    result = [-1]
    for i in range(0,n-2):
        x = sticks[n-1-i]
        y = sticks[n-2-i]
        z = sticks[n-3-i]
        if y + z > x:
            result = [z ,y ,x]
            break


    return result
