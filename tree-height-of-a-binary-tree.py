# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?isFullScreen=true

def height(root):
    leftHeight = 0
    rightHeight = 0
    
    if(root.left):
        leftHeight = height(root.left) + 1
    
    if(root.right):
        rightHeight = height(root.right) + 1
    
    if(leftHeight > rightHeight):
        return leftHeight
    else:
        return rightHeight
