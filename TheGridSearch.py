# https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true

def gridSearch(G, P):
    # Write your code here
    columns = [list(i) for i in zip(*G)]
    pattern_columns = [list(i) for i in zip(*P)]
    count = len(pattern_columns)
    match = 0
    result = "NO"
    array = []
    
    for j in range(len(columns)):
        item = "".join(columns[j])
        print(item)
        for i in range(len(pattern_columns)):
            value = "".join(pattern_columns[i])
            print(value)
            if value in item:
                array.append(item.index(value))
                match += 1
                del pattern_columns[i]
                break
        if match == count:
            result = "YES"
            break
    
    print(array)
    return result
