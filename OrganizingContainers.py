# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true

def organizingContainers(container):
    # Write your code here
    Rows = []
    Cols = []
    Works = True
    
    for i in range(len(container)):
        Rows.append(sum(container[i]))
       
            
    N = [list(i) for i in zip(*container)]     
    for i in range(n):
        Cols.append(sum(N[i]))
  
    Rows.sort()
    Cols.sort()
    if(Rows == Cols):
        return "Possible"
    else:
        return "Impossible"
