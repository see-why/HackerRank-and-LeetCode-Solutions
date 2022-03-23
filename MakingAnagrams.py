#  https://www.hackerrank.com/challenges/making-anagrams/problem?isFullScreen=true

def makingAnagrams(s1, s2):
    # Write your code here
    a = collections.Counter(s1)
    b = collections.Counter(s2)
    sum_of_commons = sum((a & b).values())
    return (len(s1)-sum_of_commons) + (len(s2)-sum_of_commons)
