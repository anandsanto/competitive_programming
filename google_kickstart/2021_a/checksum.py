import numpy as np
from collections import defaultdict

import heapq

def prims(adj_matrix: dict, complete_graph=True):
    """
    Name: prims(adj_matrix: dict, root_node, complete_graph=True)
    Args:
      - adj_matrix: Dict of dict with all the nodes and their inter-costs
      - complete_graph: Boolean indicating if the final forest should be a complete adjacency matrix,
                        that is whether parent node should be listed under the nodes that the child connects to
    """

    forest = {}
    visited = set()
    allnodes_set = set(adj_matrix.keys())

    while len(allnodes_set) > 0:
        root_node = allnodes_set.pop()
        links = [(cost, (root_node, to_node)) for to_node, cost in adj_matrix[root_node].items()]
        heapq.heapify(links)
        visited.add(root_node)

        while len(links) > 0:

            _, src_dst = heapq.heappop(links)
            if src_dst[1] not in visited:
                allnodes_set.remove(src_dst[1])
                visited.add(src_dst[1])
                if src_dst[0] not in forest:
                    forest[src_dst[0]] = []
                forest[src_dst[0]].append(src_dst[1])

                if complete_graph:
                    if src_dst[1] not in forest:
                        forest[src_dst[1]] = []
                    forest[src_dst[1]].append(src_dst[0])

                for next_node, cost in adj_matrix[src_dst[1]].items():
                    if next_node not in visited:
                        heapq.heappush(links, (cost, (src_dst[1], next_node)))

    return forest

def dfs(node, parent=None):
    curcost = 0
    children = [i for i in forest[node] if i != parent]
    for child in children:
        allnodes.remove(child)
        if node < N:
            curcost += cost[node][child-N] + dfs(child, node)
        else:
            curcost += cost[child][node-N] + dfs(child, node)
    return curcost

for t in range(1, int(input())+1):
    N = int(input())
    grid = np.array([[int(i) for i in input().split()] for j in range(N)])
    cost = [[int(i) for i in input().split()] for j in range(N)]
    r_check = [int(i) for i in input().split()]
    c_check = [int(i) for i in input().split()]

    adj_matrix = defaultdict(dict)
    sum_cost = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == -1:
                adj_matrix[r][N+c] = -1*cost[r][c]
                adj_matrix[N+c][r] = -1*cost[r][c]
                sum_cost += cost[r][c]


    forest = prims(adj_matrix)

    allnodes = set(forest.keys())
    visit = set()
    update_cost = 0
    while len(allnodes) > 0:
        root = allnodes.pop()
        update_cost += dfs(root)

    print(f"Case #{t}: {sum_cost - update_cost}")
