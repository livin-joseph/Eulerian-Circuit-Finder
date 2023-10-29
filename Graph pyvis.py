# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:33:19 2023

@author: Livin
"""

import Hierholzer, Dijkstra

from itertools import combinations

from pyvis.network import Network
import networkx as nx

pyvis_graph = Network(directed=True)

#nx_graph = nx.cycle_graph(10)
nx_graph = nx.MultiGraph()

for i in range(1,11):
    nx_graph.add_node(i, label=str(i))

nx_graph.add_edges_from([(1,2,{'weight': 1}),
                         (2,3,{'weight': 1}),
                         (3,4,{'weight': 1}),
                         (1,4,{'weight': 1}),
                         (4,5,{'weight': 1}),
                         (5,6,{'weight': 1}),
                         (4,6,{'weight': 1})])

pyvis_graph.add_node(1, label="1")
pyvis_graph.add_node(2, label="2")
pyvis_graph.add_node(3, label="3")
pyvis_graph.add_node(4, label="4")
pyvis_graph.add_node(5, label="5")
pyvis_graph.add_node(6, label="6")
pyvis_graph.add_node(7, label="7")
pyvis_graph.add_node(8, label="8")


"""
pyvis_graph.add_edge(1,2)
pyvis_graph.add_edge(3,4)
pyvis_graph.add_edges([(1,4),(1,3),(2,3),(1,1)])
"""

#pyvis_graph.from_nx(nx_graph)
"""
u, v, keys, weight = nx_graph.edges(data="weight", keys=True)
print(u,"\n",v,"\n",keys,"\n",weight)
"""
EDGES = pyvis_graph.get_edges()
# Iterate through edges and aggregate weights
for u, v, data in nx_graph.edges(data=True):
    # Check if the edge already exists in Pyvis
    #if {'value': data['weight'], 'from': u, 'to': v} not in EDGES:
    print(u,v,data)

        # If the edge doesn't exist, add it with weight as the aggregation
    pyvis_graph.add_edge(u, v, value=data['weight'], label=str(data['weight']),arrows = "hi",color = 'blue')
    EDGES = pyvis_graph.get_edges()
    #print(EDGES)

adj_list = {}
VERTICES = pyvis_graph.get_nodes()
for i in VERTICES:
    adj_list[i] = []

for i in EDGES:
    print(i)
    adj_list[i['from']].append(i['to'])
    adj_list[i['to']].append(i['from'])

print(adj_list)
Hierholzer.start(adj_list)

"""
G1 = {
    1: [2, 3, 4],
    2: [1, 3],
    3: [1, 2],
    4: [1, 5],
    5: [4]
}
G2 = {
    1: [2, 3, 4, 5],
    2: [1, 3],
    3: [1, 2],
    4: [1, 5],
    5: [1, 4]
}
G3 = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [1, 2],
    4: [1, 2, 5],
    5: [4]
}
G4 = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2],
}
G5 = {
    1: [],
    2: []
    # all degree is zero
}
"""

pyvis_graph.set_edge_smooth('horizontal')
pyvis_graph.show_buttons()
pyvis_graph.show("basic.html", notebook=False)
#pyvis_graph.write_html("basic.html", open_browser=True)


