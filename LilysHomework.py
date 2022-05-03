# https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true

def lilysHomework(arr):
    # Write your code here
    def solution(a):
        m = {}
        for i in range(len(a)):
            m[a[i]] = i 
            
        sorted_a = sorted(a)
        ret = 0
        
        for i in range(len(a)):
            if a[i] != sorted_a[i]:
                ret +=1
                
                ind_to_swap = m[ sorted_a[i] ]
                m[ a[i] ] = m[ sorted_a[i]]
                a[i],a[ind_to_swap] = sorted_a[i],a[i]
        return ret
    
    asc=solution(list(arr))
    desc=solution(list(reversed(arr)))
    return (min(asc,desc))
