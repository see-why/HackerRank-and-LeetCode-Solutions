# https://www.hackerrank.com/challenges/balanced-forest/problem?isFullScreen=true


#!/bin/python3

from operator import attrgetter
from itertools import groupby
from sys import stderr

class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.children = []
        
def readtree():
    size = int(input())
    values = readints()
    assert size == len(values)
    nodes = [Node(i, v) for i, v in enumerate(values)]
    for _ in range(size - 1):
        x, y = readints()
        nodes[x-1].children.append(nodes[y-1])
        nodes[y-1].children.append(nodes[x-1])
    return nodes

def readints():
    return [int(fld) for fld in input().strip().split()]

def findbestbal(nodes):
    if len(nodes) == 1:
        return -1
    rootify(nodes[0])
#    print([(n.index, n.value, n.totalval) for n in nodes], file=stderr)
    best = total = nodes[0].totalval
    dummynode = Node(None, None)
    dummynode.totalval = 0
    sortnode = []
    for k, g in groupby(sorted([dummynode] + nodes, key = attrgetter('totalval')), attrgetter('totalval')):
        sortnode.append(list(g))
    total = nodes[0].totalval
    for ihi, n in enumerate(sortnode):
        if 3 * n[0].totalval >= total:
            break
    else:
        assert False
    ilo = ihi - 1
    for ihi in range(ihi, len(sortnode)):
        hi = sortnode[ihi][0].totalval
        lo = sortnode[ilo][0].totalval
        while 2 * hi + lo > total:
            if lo == 0:
                return -1
            if (total - lo) % 2 == 0:
                x = (total - lo) // 2
                for lonode in sortnode[ilo]:
                    if uptototalval(lonode, x + lo):
                        return x - lo
            ilo -= 1
            lo = sortnode[ilo][0].totalval
        if len(sortnode[ihi]) > 1:
            return 3 * hi - total
        hinode = sortnode[ihi][0]
        if 2 * hi + lo == total:
            for lonode in sortnode[ilo]:
                if uptototalval(lonode, hi) != hinode:
                    return hi - lo
        y = total - 2 * hi
        if uptototalval(hinode, 2 * hi) or uptototalval(hinode, hi + y):
            return hi - y

def rootify(root):
    root.parent = root.jumpup = None
    root.depth = 0
    bfnode = [root]
    i = 0
    while i < len(bfnode):
        node = bfnode[i]
        depth = node.depth + 1
        jumpup = uptodepth(node, depth & (depth - 1))
        for child in node.children:
            child.parent = node
            child.children.remove(node)
            child.depth = depth
            child.jumpup = jumpup
            bfnode.append(child)
        i += 1
    for node in reversed(bfnode):
        node.totalval = node.value + sum(child.totalval for child in node.children)
            
def uptodepth(node, depth):
    while node.depth > depth:
        if node.jumpup.depth <= depth:
            node = node.jumpup
        else:
            node = node.parent
    return node
            
def uptototalval(node, totalval):
  try:
#    print('uptototalval(%s,%s)' % (node.index, totalval), file=stderr)
    while node.totalval < totalval:
        if node.parent is None:
            return None
        if node.jumpup.totalval <= totalval:
            node = node.jumpup
        else:
            node = node.parent
#        print((node.index, node.totalval), file=stderr)
    if node.totalval == totalval:
        return node
    else:
        return None
  except Exception:
    return None
    
ncases = int(input())
for _ in range(ncases):
    print(findbestbal(readtree()))
