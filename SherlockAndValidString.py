https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true

def isValid(s):
    # Write your code here
    c = Counter(Counter(s).values())
    if len(c)==1:
        return "YES"
    if len(c)>2:
        return "NO"
    if 1 in c.values() and (c[min(c.keys())]==1 or (max(c.keys()) - min(c.keys())==1)):
        return "YES"
    else:
        return "NO"
