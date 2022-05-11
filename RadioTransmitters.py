# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem?isFullScreen=true

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x = sorted(list(set(x)))
    n = len(x)

    count, first_uncovered = 0, 0
    while first_uncovered < n:
      i = first_uncovered
      while i < n and x[i] - x[first_uncovered] <= k:
        i += 1
      while first_uncovered < n and x[first_uncovered] - x[i - 1] <= k:
        first_uncovered += 1
      count += 1
    return count
