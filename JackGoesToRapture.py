# https://www.hackerrank.com/challenges/jack-goes-to-rapture/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from collections import deque

import heapq
#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
    n = g_nodes
    costs = [10 ** 10] * (n + 1)
    work = []
    heapq.heappush(work, (0, 1))
    
    costs[1] = 0
    
    while work:
        (current_cost, current_node) = heapq.heappop(work)
        for (neighbour, cost) in graph[current_node]:
            acc_cost = max(current_cost, cost)
            if acc_cost < costs[neighbour]:
                costs[neighbour] = acc_cost
                heapq.heappush(work, (acc_cost, neighbour))
    
    print (costs[n]) if costs[n] < 10 ** 10 else print ('NO PATH EXISTS')

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges
    
    graph = defaultdict(set)

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())
        graph[g_from[i]].add((g_to[i], g_weight[i]))
        graph[g_to[i]].add((g_from[i], g_weight[i]))

    getCost(g_nodes, g_from, g_to, g_weight)
