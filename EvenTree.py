# https://www.hackerrank.com/challenges/even-tree/problem?h_r=profile

from collections import deque

def reconstruct(tree):
    visited = [False] * len(tree)
    queue = deque([0])
    reconstructed = [list() for i in range(len(tree))]
    while len(queue) > 0:
        current = queue.popleft()
        visited[current] = True
        for i in tree[current]:
            if not visited[i]:
                reconstructed[current].append(i)
                queue.append(i)
    return reconstructed

cuts = 0
def dfs(tree, index):
    global cuts
    subtrees = []
    for i in tree[index]:
        subtrees.append(dfs(tree, i))
    for vertices in subtrees[:]:
        if not vertices % 2:
            cuts += 1
            subtrees.remove(vertices)

    return sum(subtrees) + 1



# Complete the evenForest function below.
def evenForest(tree):
    tree = reconstruct(tree)
    dfs(tree, 0)
    return (cuts)
