# https://www.hackerrank.com/challenges/maximum-xor/problem?isFullScreen=true

def maxXor(arr, queries):
    # solve here
    ans = []
    trie = {}
    k = len(bin(max(arr+queries))) - 2 
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for char in number:
            node = node.setdefault(char, {})
    for n in queries:
        node = trie
        s = ''
        for char in'{:b}'.format(n).zfill(k) :
            tmp = str(int(char) ^ 1) 
            tmp = tmp if tmp in node else char 
            s += tmp 
            node = node[tmp]
        ans.append(int(s, 2) ^ n) 
    return ans
