# https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true

def myFunc(a):
  return int(a)
  
def bigSorting(unsorted):
    # Write your code here
    unsorted.sort(key=myFunc)
    return unsorted
