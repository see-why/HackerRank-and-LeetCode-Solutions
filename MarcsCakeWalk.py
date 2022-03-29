# https://www.hackerrank.com/challenges/marcs-cakewalk/problem?isFullScreen=true

def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort()
    calorie.reverse()

    miles=0
    for i in range(n):
        cup=calorie[i]*(2**i)
        miles+=cup
    
    return miles
