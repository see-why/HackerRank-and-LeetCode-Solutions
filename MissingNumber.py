# https://leetcode.com/problems/missing-number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        nums.sort()
        
        for i in range(size+1):
            if i not in nums:
                return i
            
