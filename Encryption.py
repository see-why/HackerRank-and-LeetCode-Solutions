# https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true

def encryption(s):
    # Write your code here
    s = s.replace(" ","")
    size = len(s)
    square_root = math.sqrt(size)
    row = math.floor(square_root)
    column = math.ceil(square_root)
    
    result = defaultdict(str)
    
    for i in range(0, size, column):        
        last_index = min(size,i+column)
        entry = s[i:last_index]
        for j in range(len(entry)):
            result[j] += entry[j]
    
    result = list(result.values())
    return(" ".join(result))
