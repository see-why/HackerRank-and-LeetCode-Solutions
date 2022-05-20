# https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true


def dfs(graph, start, visited):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    graph = {i: set() for i in range(1,n+1)}
    for city1, city2 in cities:
        graph[city1].add(city2)
        graph[city2].add(city1)

    # if libraries are cheaper than roads, build 
    #   library in every city and build no roads
    if c_lib < c_road:
        return c_lib * n

    # determine number of connected components (CC) in graph
    visited = set()
    nCC = 0
    for city in range(1, n+1):
        if city not in visited:
            dfs(graph, city, visited)
            nCC += 1

    # 1 library per CC, nCitiesPerCC-1 roads per CC
    return nCC*c_lib + (n-nCC)*c_road
