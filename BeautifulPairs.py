# https://www.hackerrank.com/challenges/beautiful-pairs/problem?isFullScreen=true

def beautifulPairs(A, B):
    # Write your code here
    a_dict = collections.Counter(A)
    b_dict = collections.Counter(B)
    count = 0
    
    for key in a_dict.keys():
        if key in b_dict.keys():
            count += min(a_dict[key],b_dict[key])
    
    if count < len(A): # instruction insist that we must make 1 change
        count += 1 # in this case the pairwise disjoint beautiful pairs increase by one cause we made an extra match
    else:
        count -= 1 # in this case the pairwise disjoint beautiful pairs decrease by one cause our change removes a match
    
    return count
