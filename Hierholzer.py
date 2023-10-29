# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:12:46 2023

@author: livin
"""

# Eulerian Path is a path in graph that visits every edge exactly once.
# Eulerian Circuit is an Eulerian Path which starts and ends on the same
# vertex.
# time complexity is O(V+E)
# space complexity is O(VE)


# using dfs for finding eulerian path traversal
def dfs(u, graph, visited_edge, path=[]):
    path = path + [u]
    print(path)
    for v in graph[u]:
        if visited_edge[u][v] == False and v not in path:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    for v in graph[u]:
        if visited_edge[u][v] == False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path


# for checking in graph has euler path or circuit
def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph.keys():
            continue
        if len(graph[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node


def check_euler(graph, max_node):
    #2D List to mark visited and unvisited edges
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("graph is not Eulerian")
        print("no path")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("graph has a Euler path")
    if check == 1:
        print("graph has a Euler circuit")
    path = dfs(start_node, graph, visited_edge)
    print(path)


def start(G):
    max_node = 10
    check_euler(G, max_node)
