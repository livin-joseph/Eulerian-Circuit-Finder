# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:12:46 2023

@author: livin
"""

# Eulerian Path is a path in graph that visits every edge exactly once.
# Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex.
# time complexity is O(V+E)
# space complexity is O(VE)


# using dfs for finding eulerian path traversal
def dfs(u, adj_list, visited_edge, path=[]):
    path = path + [u]
    print(path)
    for v in adj_list[u]:
        if visited_edge[u][v] == False and v not in path and len(adj_list[v]) % 2 != 1:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, adj_list, visited_edge, path)
    for v in adj_list[u]:
        if visited_edge[u][v] == False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, adj_list, visited_edge, path)
    return path


# for checking in graph has euler path or circuit
def check_circuit_or_path(adj_list, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in adj_list.keys():
            continue
        if len(adj_list[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node


def check_euler(adj_list, max_node):
    #2D List to mark visited and unvisited edges
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(adj_list, max_node)
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
    path = dfs(start_node, adj_list, visited_edge)
    print(path)

def make_euler(adj_list, adj_matrix):
    odd_count = 0
    odd_vertices = []
    for i in adj_list:
        if len(adj_list[i]) % 2 == 1:
            odd_count = odd_count + 1
            odd_vertices.append(i-1)
    print("Odd degree vertices: ",odd_vertices)
    if odd_count == 0:
        return 0, 0, 0
    import Dijkstra
    s_dist, sp = Dijkstra.dijkstra(adj_matrix, odd_vertices[0], odd_vertices[1])
    for i in range(0,len(sp)):
        sp[i] = sp[i] + 1
    print("Shortest path between odd degree vertices: ",sp)
    return odd_count, s_dist, sp

def start(adj_list,adj_matrix):
    max_node = 10
    odd_count, s_dist, sp = make_euler(adj_list,adj_matrix)
    check_euler(adj_list, max_node)
    return odd_count, s_dist, sp
