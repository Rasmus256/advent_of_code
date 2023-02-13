import networkx as nx
import os

edges = []

def getDecendants(graph, node, succ = []):
    for g in G.successors(node):
        if not g in succ:
            succ.append(g)
            getDecendants(graph, g, succ)
    return succ

def getRelevantEdges(nodes, edges):
    return list((f"{x[0]} -> {x[1]}" for x in edges if x[0] in nodes and x[1] in nodes))

def getAncestors(graph, node, succ = []):
    for g in G.predecessors(node):
        if not g in succ:
            succ.append(g)
            getAncestors(graph, g, succ)
    return succ

def getRelated(graph, node, succ = []):
    toVisit = list(G.predecessors(node)) + list(G.successors(node))
    for g in toVisit:
        if not g in succ:
            succ.append(g)
            getRelated(graph, g, succ)
    return succ

G=nx.DiGraph()
numNodes = int(os.getenv("NUM_NODES"))
startNodes = os.getenv("START_NODE")
print(f"STARTED with parameters NUM_NODES: {numNodes}, START_NODE: {startNodes}")
G.add_nodes_from(map(lambda x: str(x), range(numNodes)))
    
file1 = open('edges.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    fromAndTo = line.strip().split(",")
    edges.append(fromAndTo)
    G.add_edge(fromAndTo[0],fromAndTo[1])
    
def handleSingleNode(startNode):
    print(f"--- begin {startNode} ---")    
    decendants = getDecendants(G, startNode)
    ancestors = getAncestors(G, startNode)
    related = getRelated(G, startNode)

    print(f"{startNode} has these ancestors: {ancestors}")
    print(f"these edges are involved with ancestors: {getRelevantEdges(ancestors, edges)}")
    print(f"{startNode} has these decendents: {decendants}")
    print(f"these edges are involved with decendents: {getRelevantEdges(decendants, edges)}")
    print(f"{startNode} has related: {related}")
    print(f"these edges are involved with related: {getRelevantEdges(related, edges)}")
    print(f"--- end {startNode} ---")    
    
map(handleSingleNode, startNodes.split(','))
