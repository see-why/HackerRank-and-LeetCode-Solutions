# https://www.hackerrank.com/challenges/cut-the-tree/problem?isFullScreen=true

cum_weight=dict()

child_parent=dict()

min_t=[float('inf')]

def dfs_iterative(G, s, weights):
    total = sum(weights)

    stack = [s]
    visited = set()

    while stack:
        vertex = stack[-1]
        if vertex in visited:
            # logic
            # cum sum of a node: it's weight+ all it's children's weight
            # logic
            cum_weight[vertex]=weights[vertex-1]
            for c in G[vertex]:
                if child_parent.get(c,-1)==vertex:
                    cum_weight[vertex]+=cum_weight[c]
            # difference
            min_t[0]=min(
                min_t[0],
                abs(total-2*cum_weight[vertex])
            )
            stack.pop()
            continue
        visited.add(vertex)
        for neighbor in G[vertex]:
            if neighbor not in visited:
                child_parent[neighbor]=vertex
                stack.append(neighbor)
    
    return visited

def setGraph(nCount, edges):
    """
    Boilerplate method to set graph
    returns graph
    :param: nCount number of nodes in graph - n nodes
    :param: edges list of edges in graph
    """
    g=dict()

    # setting the nodes
    # create dict with key and value as node
    for _t,_e in edges:
        if _t not in g.keys():
            g[_t]=[_e]
        else:
            g[_t].append(_e)
        if _e not in g.keys():
            g[_e]=[_t]
        else:
            g[_e].append(_t)
    
    # updates the dict for zombie nodes
    g.update({k:[] for k in range(1,nCount+1) if k not in g.keys()})
    
    return g


def cutTheTree(data, edges):
    # Write your code here
    G=setGraph(len(data),edges)
    print(G)
    dfs_iterative(G,1,data) #<- 1 will act as root node # with the maximum cumulative sum
    return min_t[0]
