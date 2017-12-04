
# -*- coding: utf-8 -*-

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

toggle = True
G = nx.Graph()
H = {}
j = 0

def Prim(G = nx.Graph(), R = None):
    i = 0
    Q  = {}
    predecessor = {}

    for v,data in G.nodes(data=True):
        Q[v] = np.inf
        predecessor[v] = 'null'    
    
    Q[R] = 0.0 
    MST  = nx.create_empty_copy(G) 

    while Q:
        u = min(Q,key = Q.get)
        del Q[u]
        
        for vizinho in G[u]:
            if vizinho in Q:
                if G[u][vizinho]['weight'] < Q[vizinho]:
                    predecessor[vizinho] = u 
                    Q[vizinho] = G[u][vizinho]['weight'] 

        if predecessor[u] is not 'null':
            for v1,v2,data in G.edges(data=True):
                if (v1 == predecessor[u] and v2 == u):
                    MST.add_edge(v1,v2, weight=data['weight']) 
                    H[i] = MST.copy() 
                    i = i + 1
                elif (v1 == u and v2 == predecessor[u]):
                    MST.add_edge(v2,v1, weight=data['weight'])
                    H[i] = MST.copy()
                    i = i + 1

def onclick(event):
    global toggle
    global j
   
    event.canvas.figure.clear()

    if toggle:
        labels = {}
        for v1,v2,data in G.edges(data=True):
            labels[(v1,v2)] = data['weight']
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, labels)
        toggle = not toggle
    
    else:
        labels = {}
	for v1,v2,data in H[j].edges(data=True):
            labels[(v1,v2)] = data['weight']
        nx.draw(H[j], pos, with_labels=True)
        nx.draw_networkx_edge_labels(H[j], pos, labels)
        j = j + 1

    event.canvas.draw()

A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)

Prim(G, 0)

pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
