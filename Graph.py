# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:32:58 2023

@author: Livin
"""

import networkx as nx
import matplotlib.pyplot as plt
#import numpy as np

def validate(e):
    if e[0] in vertices and e[1] in vertices:
        return True
    else:
        return False

def degree(v):
    n = 0
    for e in edges:
        if v in e:
            n = n + 1
    return n

vertices = []
edges = []

print("Enter the vertices of the graph (Enter 0 to stop)")
v = input()
while v != "0":
    vertices = vertices + [v]
    v = input()

print("Enter the edges of the graph (Enter 0 to stop)")
e = input()
while e != "0":
    if validate(e):
        edges = edges + [e]
    else:
        print("Invalid edge")
    e = input()

g = nx.Graph()
for i in vertices:
    g.add_node(i)

for j in edges:
    g.add_edge(j[0],j[1])

nx.draw_networkx(g)

numberOfOddVertices = 0
for i in vertices:
    if degree(e) % 2 == 1:
        numberOfOddVertices = numberOfOddVertices + 1

if numberOfOddVertices == 0:
    print("Eulerian Graph")
elif numberOfOddVertices == 2:
    print("Semi-Eulerian Graph")
else:
    print("Non-Eulerian Graph")

"""
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
#g.add_node(5)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(2,2)

nx.draw_networkx(g)

#fig, ax = plt.subplots()  # Create a figure and axis
#nx.draw(g, with_labels=True, ax=ax)  # Use ax to draw the graph
"""