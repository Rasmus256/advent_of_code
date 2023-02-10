import networkx as nx
import random

def getAncestors(graph, node):
    getChildren(graph, node, [])
def getChildren(graph, node, succ):
    for g in G.successors(node):
        if not g in succ:
            succ.append(g)
            succ.append(getChildren(graph, g, succ))
    return succ    

def getDecendants(graph, node):
    getParents(graph, node, [])
def getParents(graph, node, succ):
    for g in G.predecessors(node):
        if not g in succ:
            succ.append(g)
            succ.append(getParents(graph, g, succ))
    return succ    

G=nx.DiGraph()
G.add_nodes_from([1])
int = 10
for i in range(int):
    G.add_node(i+1)
for i in range(int):
    G.add_edge(i, i+1)
    
decendants = getDecendants(G, 5)
ancestors = getAncestors(G, 5)

print(f"5 has these ancestors: {ancestors} and these decendents: {decendants}")

print(nx.to_dict_of_dicts(G))
