# https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true


def commonChild(s1 , s2):
    # Write your code here   
    last_row = [0]*(len(s1)+1)

    for i in range(1, len(s1)+1):
        current = [0]
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                current.append(last_row[j-1]+1)
            else:
                current.append(max(last_row[j], current[-1]))
        last_row = current

    return last_row[-1]
