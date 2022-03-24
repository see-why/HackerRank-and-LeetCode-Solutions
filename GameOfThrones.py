# https://www.hackerrank.com/challenges/game-of-thrones/problem?isFullScreen=true

def gameOfThrones(s):
    # Write your code here
    dict = collections.Counter(s)
    max_value = max(dict.values())
    
    if(max_value == 1):
        return 'NO'
        
    result = 'YES'
    counter = 0
    
    for k, v in sorted(dict.items()):
        if(v%2 == 1):
            counter += 1
        if (counter >= 2):
            result = 'NO'
            break
    
    return result
