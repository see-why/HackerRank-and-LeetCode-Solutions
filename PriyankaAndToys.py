#  https://www.hackerrank.com/challenges/priyanka-and-toys/problem?isFullScreen=true

def toys(w):
    # Write your code here
    count = 0
    i=0

    w.sort()
    N = len(w)

    while i < N:
            container = [value for value in w if value <= (w[0] + 4) and value >= w[0]]
            w = w[len(container):]
            if container.count > 0:
                i += len(container)
                count += 1

    return count
