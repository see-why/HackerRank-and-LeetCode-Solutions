# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

def biggerIsGreater(w):
    # Write your code here
    w = list(w[::-1])
    for i in range(1,len(w)):
        if w[i-1] > w[i]:
            for j in range(i):
                if w[j] > w[i]:
                    w[j],w[i] = w[i],w[j]
                    w = sorted(w[:i])[::-1] + w[i:]
                    return "".join(w[::-1])
                    break
            break
    else:
        return "no answer"
