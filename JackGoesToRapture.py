# https://www.hackerrank.com/challenges/jack-goes-to-rapture/problem?h_r=profile

def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
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
    
    return costs[n] if costs[n] < 10 ** 10 else 'NO PATH EXISTS'
