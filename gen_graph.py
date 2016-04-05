#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import networkx as nx

# load nodes
NODE_TYPE_FILTER = ('officer', 'entity')
G = nx.Graph()
with open("data-012314/nodesNW.csv", "rb") as fp:
    fp.readline()
    reader = csv.reader(fp, delimiter=";")
    count = 0
    for row in reader:
        nodetype = row[1].lower()
        if nodetype in NODE_TYPE_FILTER:
            G.add_node(row[0], label=row[2].strip(), type=nodetype)
        count += 1
print count, "nodes loaded"

# exclude entity officers
EXCL_OFFICER_NAME = ["limited", "ltd", "trust", "corp", "inc", "bearer",
        "holding"]
excl_nodes = []
for n in G.nodes_iter():
    nattr = G.node[n]
    if nattr['type'] == 'officer':
        label = nattr['label'].lower()
        found = False
        for name in EXCL_OFFICER_NAME:
            if name in label:
                found = True
                break
        if found:
            excl_nodes.append(n)
for n in excl_nodes:
    G.remove_node(n)

# load edges
EDGE_TYPE_FILTER = ('shareholder', 'related company')
with open("data-012314/edges_1DNW.csv", "rb") as fp:
    fp.readline()
    reader = csv.reader(fp, delimiter=';')
    count = 0
    for row in reader:
        edgetype = row[3].lower()
        if row[1] in G and row[2] in G and edgetype in EDGE_TYPE_FILTER:
            G.add_edge(row[1], row[2], label=edgetype)
            count += 1
print count, "edges loaded"

# remove zero-degree nodes
G = G.subgraph([n for n, d in G.degree_iter() if d > 0])
print G.order()
print G.size()

# betweenness centrality
#bb = nx.betweenness_centrality(G)
#nx.set_node_attributes(G, "betweenness", bb)

# save
#nx.write_gexf(G, "g2.gexf")
