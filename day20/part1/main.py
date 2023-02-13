import networkx as nx
import random
import os

def getDecendants(graph, node):
    return getChildren(graph, node, [])
def getChildren(graph, node, succ):
    for g in G.successors(node):
        print(f"viting {g}" )
        if not g in succ:
            succ.append(g)
            getChildren(graph, g, succ)
    return succ    
edges = []
def getRelevantEdges(nodes):
    global edges
    filtered = []
    for edge in edges:
        if int(edge[0]) in nodes or int(edge[1]) in nodes:
            filtered.append(f"{edge[0]} --> {edge[1]}")
    return filtered
    

def getAncestors(graph, node):
    return getParents(graph, node, [])
def getParents(graph, node, succ):
    for g in G.predecessors(node):
        print(f"viting {g}" )
        if not g in succ:
            print(f"{g} is visited for the first time!" )
            succ.append(g)
            getParents(graph, g, succ)
    return succ    
def getRelated(graph, node):
    return getFamily(graph, node, [])
def getFamily(graph, node, succ):
    toVisit = []
    for g in G.predecessors(node):
        toVisit.append(g)
    for g in G.successors(node):
        toVisit.append(g)
    for g in toVisit:
        if not g in succ:
            succ.append(g)
            getFamily(graph, g, succ)
    return succ    

G=nx.DiGraph()
numNodes = int(os.getenv("NUM_NODES"))
startNode = os.getenv("START_NODE")
print(f"STARTED with parameters NUM_NODES: {numNodes}, START_NODE: {startNode}")
for i in range(numNodes):
    G.add_node(str(i+1))
    
file1 = open('edges.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    fromAndTo = line.strip().split(",")
    edges.append(fromAndTo)
    G.add_edge(fromAndTo[0],fromAndTo[1])
    
decendants = getDecendants(G, startNode)
ancestors = getAncestors(G, startNode)
related = getRelated(G, startNode)

print(f"5 has these ancestors: {ancestors} and these decendents: {decendants}")
related = getRelated(G, startNode)
print(f"5 has related: {related}")

print(f"these adges are involved: {getRelevantEdges(related)}")


print(nx.to_dict_of_dicts(G))
