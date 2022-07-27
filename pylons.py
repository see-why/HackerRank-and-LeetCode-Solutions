# https://www.hackerrank.com/challenges/pylons/problem?isFullScreen=true

def get_min(x,k,lights):        
    best = -1
    best_ind=None
    for ind,i in enumerate(lights):
        #if abs(x - i)<k:
        if -k < x - i < k:
            best=i
            best_ind=ind
        elif i>x+k:
            break
    return best,best_ind

def pylons(k, arr):
    # Write your code here
    lights = [i for i,val in enumerate(arr) if val==1]
    
    pos=0
    best=None
    best_ind=None
    count=0
 
    while 1:                                
            
        if pos>=n:
            break
        
        if best==lights[-1]:
            count=-1
            break
                       
        if best_ind==None:
            best,best_ind = get_min(pos,k,lights)
        else:
            lights = lights[(best_ind+1):]
            best,best_ind = get_min(pos,k,lights)
        
        if best==-1:
            count=-1
            break
        
        count+=1
        pos = best + k                                            

    
    return(count)
