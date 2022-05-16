# https://www.hackerrank.com/challenges/short-palindrome/problem?isFullScreen=true

def shortPalindrome(s):
    # Write your code here
    arr1 = [0]*26
    arr2 = [[0]*26 for i in range(26)]
    arr3 = [0]*26
    
    ans = 0
    for i in range(len(s)):
        idx = ord(s[i]) - ord('a')
        ans += arr3[idx]
        for j in range(26):
            arr3[j] += arr2[j][idx]
        for j in range(26):
            arr2[j][idx] += arr1[j]
        arr1[idx] += 1
    return ans % (10**9+7)
