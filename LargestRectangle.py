# https://www.hackerrank.com/challenges/largest-rectangle/problem?isFullScreen=true

def largestRectangle(h):
    # Write your code here
    h += [0]
    s = []
    ma = 0
    for i in range(0, len(h)):
        j = i
        while len(s) > 0 and s[-1][0] >= h[i]:
            val, j = s.pop()
            ma = max(ma, (i - j) * val)
        s.append([h[i], j])
    return ma
