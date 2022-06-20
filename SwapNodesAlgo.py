# https://www.hackerrank.com/challenges/swap-nodes-algo/problem?isFullScreen=true

def swapNodes(indexes, queries):
    #
    # Write your code here.
    #

    #modifying the recursion limit in python because of #10 and #11
    sys.setrecursionlimit(1500)
    #tree node
    class Node:
        def __init__(self, data, level):
            self.data = data
            self.left = None
            self.right = None
            self.level = level
    #traverse the tree in order
    def traverse_inorder(tree):
        if tree.left:
            traverse_inorder(tree.left)
        item.append(tree.data)
        if tree.right:
            traverse_inorder(tree.right)
    #building the tree
    def create_tree(indexes):
        from queue import Queue
        #using queue to create the tree: BFS
        q = Queue()
        root = Node(1, 1)
        maxlevel = 1
        q.put(root)
        for left, right in indexes:
            cur = q.get()
            if left != -1:
                leftNode = Node(left, cur.level + 1)
                cur.left = leftNode
                q.put(leftNode)
            if right != -1:
                rightNode = Node(right, cur.level + 1)
                cur.right = rightNode
                q.put(rightNode)
            #Finally the q is empty, and cur is at lowest level. Because there are always [-1, -1]s at the end of the indexes
            maxlevel = cur.level
        return (root, maxlevel)

    #swaping respectively
    def swap_tree(tree, ks):
        if tree.left:
            swap_tree(tree.left, ks)
        if tree.right:
            swap_tree(tree.right, ks)
        if tree.level in ks:
            tree.left, tree.right = tree.right, tree.left
        return tree


    tree, maxlevel = create_tree(indexes)
    ret = []
    for k in queries:
        item = []
        #list comprehensions
        ks = [x for x in range(1, maxlevel+1) if x%k==0]
        root = swap_tree(tree, ks)
        traverse_inorder(root)
        ret.append(item)
    return ret
