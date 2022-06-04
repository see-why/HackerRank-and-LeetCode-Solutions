https://www.hackerrank.com/challenges/abbr/problem?isFullScreen=true

def abbreviation(a, b):
    # Write your code here
    bpos = {}
    for i in range(len(b)):
        bpos[b[i]] = (bpos[b[i]] | set([i])) if b[i] in bpos else set([i])
    possibilities = set([0])
    for i in range(len(a)):
        if a[i].upper() in bpos:
            intersection = bpos[a[i].upper()] & possibilities
            advancement = set([i + 1 for i in intersection])
        else:
            advancement = set([])
        if a[i].upper() == a[i]:#capitals must follow the intersection
            possibilities = advancement
        else:
            possibilities = possibilities | advancement
    return ("YES" if (len(b)) in possibilities else "NO")
