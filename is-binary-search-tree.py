# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?isFullScreen=true

def checkBST(root):
        return check_BST_subtree(root, -1, 10001)    
    
def check_BST_subtree(root, min_value, max_value):
    if(root == None): return True
    
    data = root.data
    
    if(min_value < data < max_value):
        return check_BST_subtree(root.left, min_value, data) and check_BST_subtree(root.right, data, max_value)
    else:
        return False
