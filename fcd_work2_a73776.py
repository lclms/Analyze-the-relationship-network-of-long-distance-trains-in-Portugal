#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 11:58:42 2018

@author: Luis Marques
"""

import matplotlib.pyplot as plt
import pandas as pd
import csv
import networkx as nx
import operator



# funcao para importar e criar o grafo
def graph_func():
    
    g = nx.Graph()    
    g = nx.Graph(name="Train Graph Network")    
    with open('dataset.csv', 'r', encoding='utf-8') as data:
           reader = csv.reader(data)
           for row in reader:
               g.add_edge(*row)
    return g

# chamar a funcao 
g = graph_func()
# info of graph
print(nx.info(g))

# mostrar graficamente o grafo
plt.figure(figsize=(10, 10))
plt.title("Graph Network")
nx.draw(g, node_size = 250, node_color='red', with_labels=True) 
nx.draw_networkx_labels(g)
plt.show()

# degree distribution
degree_distribution = nx.degree_histogram(g)
d_h = pd.DataFrame(degree_distribution)

ax = d_h.plot(kind = 'bar', legend = False)
plt.title("Degree Distribution")
ax.set_xlabel("Degree")
ax.set_ylabel("Frequency")
plt.show()




# betweenness centrality
bc = nx.betweenness_centrality(g)

print(sorted(nx.betweenness_centrality(g).items(),key=operator.itemgetter(1),
reverse=True))

# closeness centrality
print(sorted(nx.closeness_centrality(g).items(),key=operator.itemgetter(1),
reverse=True))


# degree centrality 

print(sorted(nx.degree_centrality(g).items(),key=operator.itemgetter(1),
reverse=True))

d = nx.degree(g)

d_d = {'1': 3, '5': 2, '17': 4, '2': 3, '3': 4, '56': 5, '4': 3, '53': 6, '7': 2, '8': 2, '9': 2, '24': 2, '10': 1, '42': 2, '11': 2, '14': 1, '12': 2, '44': 3, '15': 2, '41': 4, '16': 3, '26': 2, '27': 2, '18': 4, '25': 3, '28': 3, '19': 2, '29': 3, '20': 1, '21': 2, '31': 2, '23': 1, '49': 3, '52': 2, '54': 3, '30': 1, '22': 1, '32': 3, '33': 1, '34': 2, '35': 2, '36': 1, '47': 3, '37': 2, '38': 2, '39': 2, '40': 1, '43': 3, '45': 2, '46': 2, '13': 1, '48': 1, '50': 1, '51': 2, '6': 1, '55': 1}

ld = []

for key, value in d_d.items():    
    ld.append(value)


degree = nx.degree(g)
plt.hist(ld, bins = 10)
plt.title("Degree Values Graph")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

# densidade
nx.density(g)

# densidade para um nó
ego = nx.ego_graph(g, '53')
nx.density(ego)

# reciprocidade
und_graph = g.to_undirected()
reciprocity = float(nx.number_of_edges(und_graph)/nx.number_of_edges(g))
print(reciprocity)

# Analise no 53
ego_net = nx.ego_graph(g, "53", 1)

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(ego_net)
nx.draw_networkx(ego_net, pos, with_labels=True, node_size=800, alpha=1, node_color='r')

ego_net.size()

# Eigenvector Centrality
print(sorted(nx.eigenvector_centrality(g).items(),key=operator.itemgetter(1)
, reverse=True))

# top 5
eigen_cent = nx.eigenvector_centrality(g)
all_eigen = sorted(eigen_cent.items(), key=operator.itemgetter(1), reverse=True)
for node in all_eigen[0:5:]: 
    print("%s: %0.3f" % node)



# PageRank

pr = nx.pagerank(g)
all_pr = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)
for node in all_pr[0:5:]: 
    print("%s: %0.3f" % node)



# Cliques
fb = nx.read_edgelist("dataset.txt", create_using=nx.Graph(), nodetype=int)

cliques = [x for x in nx.find_cliques(fb)]

pos = nx.spring_layout(fb)
plt.figure(figsize=(12,12))
plt.axis('off')
nx.draw_networkx(fb, pos=pos, with_labels=True, node_size=200)


cliques

n_cliques =len(cliques)
print(n_cliques)

sizes_of_cliques = [len(x) for x in cliques]
print(sizes_of_cliques)

maximum_clique_size = max(sizes_of_cliques) 
print(maximum_clique_size)

maximu_cliques = [x for x in cliques if len(x) == maximum_clique_size]
print(maximu_cliques)


n_maximum_cliques = len(maximu_cliques)
print(n_maximum_cliques)

average_clique_size = sum(sizes_of_cliques)/n_cliques 
print(average_clique_size)

maximum_clique_sets = [set(x) for x in maximu_cliques]
print(maximum_clique_sets)


# Clustering Coefficient

nx.clustering(g)

nx.average_clustering(g)

ego_net = nx.ego_graph(g, "53")
len(ego_net)

nx.average_clustering(ego_net)

plt.figure(figsize=(8,8))
pos = nx.random_layout(ego_net)
nx.draw_networkx(ego_net, pos, node_size=300, with_labels=True)


nx.clustering(ego_net)


