# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_r=profile


def makeAnagram(a, b):
    # Write your code here
    return len(a)+len(b)-sum((Counter(a) & Counter(b)).values())*2
