# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
class Solution(object):
    result = []
    def getSmallest(self, root, k): 
        global y
        
        if root != None:
            
            left = self.getSmallest(root.left)        
        
            if left != None:
                self.result.append(left.val)
        
            y -=1
            if y == 0:
                self.result.append(root.val)
            
            right = self.getSmallest(root.right)

        
        
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        print(root)
        
        global y
        y = k
        
        self.getSmallest(root)
        print(self.result)
        
        if self.result == None:
            return None
        else:
            return self.result[len(self.result)-1]
