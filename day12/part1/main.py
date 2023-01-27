import sys
import math

class Dijkstra:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.vertices = list(graph.keys())

        # distance: minimum distance from start vertex
        self.vertex_labels = {vertex: {'distance': math.inf, 'prev': '-'} for vertex in self.vertices}

        # Obviously, the start vertex has no distance from itself
        self.vertex_labels[start_vertex]['distance'] = 0


    def _get_edge_weight(self, vertex1, vertex2):
        try:
            return self.graph[vertex1][vertex2]
        except KeyError:
            return math.inf


    def _set_label(self, vertex, weight, prev=''):
        self.vertex_labels[vertex]['distance'] = weight

        if prev:
            self.vertex_labels[vertex]['prev'] = prev


    def _get_label(self, vertex):
        return self.vertex_labels[vertex]


    def dijkstra(self):
        interiors = [self.start_vertex]
        max_interior_vertices = len(self.vertices)

        while True:
            exteriors = [vertex for vertex in self.vertices if vertex not in interiors]
            print("ext: ", len(exteriors), " ", len(interiors))
            # Nearest vertex to start vertex
            nearest_vertex = '-'

            # Distance from start index
            nearest_vertex_distance = math.inf
            for exterior in exteriors:
                exterior_label = self._get_label(exterior)

                # Shortest discovered distance of current outerior from start vertex
                shortest_discovered_distance = exterior_label['distance']

                # Last vertex through which we reached current exterior with shortest distance
                choosen_prev = exterior_label['prev']

                for interior in interiors:
                    # Shortest discovered distance of current interior from start vertex + distance of current interior from current exterior
                    distance_from_exterior = self._get_label(interior)['distance'] + self._get_edge_weight(interior, exterior)

                    if distance_from_exterior < shortest_discovered_distance:
                        shortest_discovered_distance = distance_from_exterior
                        choosen_prev = interior
            
                self._set_label(exterior, shortest_discovered_distance, choosen_prev)

                # Attempt to find the nearest exterior to start vertex
                if shortest_discovered_distance < nearest_vertex_distance:
                    nearest_vertex_distance = shortest_discovered_distance
                    nearest_vertex = exterior
            interiors.append(nearest_vertex)

            if len(interiors) == max_interior_vertices:
                break


    def build_path(self, vertex):
        if vertex == '-':
            return []
        
        return self.build_path(self.vertex_labels[vertex]['prev']) + [vertex]
def ordOfNode(str):
    val = str
    if str == "S":
        val = "a"
    elif str == "E":
        val = "z"
    return ord(val)


testInput = [
"SbcdefghijklmnopqrstuvwxyzE",
"SbcdefghijklmnopqrstuvwxyzE",
"SbcdefghijklmnopqrstuvwxyzE",
"SbcdefghijklmnopqrstuvwxyzE",
"SbcdefghijklmnopqrstuvwxyzE",
"SbcdefghijklmnopqrstuvwxyzE",
]

dumbInput = [
    "Sbc",
    "fed",
    "ghE"
]


realInput = [
"abcccaaaaaaccccccccaaaaaccccccaaaaaaccccccaaaaaaaacccaaaaaaaccaaaacccccccccccccccccccccccccaaaaaacccccccccccccccccccccccccccccaaaaaa",
"abcccaaaaaacccccccaaaaaaccccaaaaaaaacccccccaaaaaaaaaaaaaaaaccaaaaacccccccccccccccccccccccccaaaaaacccccccccccccccccccccccccccccaaaaaa",
"abccccaaaaacaaaccaaaaaaaacccaaaaaaaaacccccccaaaaaaaaaaaaaaaacaaaaaacccccccccaaacccccccccccaaaaaaaaccccccccccaaccccccccccccccccaaaaaa",
"abccccaaaaccaaaaaaaaaaaaacccaaaaaaaaaacccccaaaaaaaaaaaaaaaaaaacaaaacccccccccaaaacccccccccaaaaaaaaaacccccccccaaaccccccccccccccccccaaa",
"abcccccccccaaaaaacccaacccccccccaaacaaaccccccaacccccccaaaaaaaaacaacccccccccccaaaacccccccccaaaaaaaaaacccccccccaaaccacaaccccccccccccaaa",
"abcccccccccaaaaaacccaacccccccccaaacccccccccccccccccccaaaacaaaacccccccaacaaccaaaccccccccccaccaaaaacacccccccccaaaacaaaaccccccccccccaac",
"abccccccccccaaaaacccccccccccccccacccaaaacccccccccccccaaaacccccccccccccaaaacccccccccccaacccccaaaaccccccccjjjjaaaaaaaaaccccccccccccccc",
"abccccccccccaaaacccccccccccccccccccaaaaacccccccccccccaaaccccccccccccccaaaaacccccccccaaaaaacccaaccccccccjjjjjjkkaaaacccccccccaacccccc",
"abcccccaaccccccccccccccccccccccccccaaaaaacccccccccccccaacccccccccccccaaaaaaccccccccccaaaaaccccccccccccjjjjjjjkkkkaacccccaacaaacccccc",
"abccaaaacccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccaaaacaccccccccaaaaaaaccccaacccccjjjjoooookkkkkkkklllaaaaaaacccc",
"abccaaaaaacccccccccccccccccccccccccaaaaacccccccccccccccccccccccccccccccaaccccccccccaaaaaaaaccaaaaccccjjjoooooookkkkkkkllllaaaaaacccc",
"abcccaaaaacccccccccccccccccccccccccccaaaccccccccaaaacccccccccccccccccccccccccccccccaaaaaaaaccaaaaccccjjooooooooppkkppplllllaccaacccc",
"abccaaaaaccccccccccccaccccccccccccccccccccccccccaaaacccccccccccccccccccccccccccccccccaaacacccaaaacccijjooouuuuoppppppppplllccccccccc",
"abcccccaacccccccccccaaaaaaaaccccccccccccccccccccaaaaccccaaccccccccaaacccccccccccccaacaaccccccccccccciijoouuuuuuppppppppplllcccaccccc",
"abcccccccccccccccccccaaaaaaccccccccccccccccccccccaaccccaaaacccccccaaaaccccccccccaaaaaaccccccccccccciiiiootuuuuuupuuuvvpppllccccccccc",
"abcccccccccccccccccccaaaaaaccaaaaacccccccccccccccccccccaaaacccccccaaaaccccccccccaaaaaaccccccccccccciiinnotuuxxxuuuuvvvpppllccccccccc",
"abccccccccccccccacccaaaaaaaacaaaaaaacccccccccccccccccccaaaacccccccaaacccccaaaaccaaaaaccccaaccccccciiiinnnttxxxxuuyyyvvqqqllccccccccc",
"abcccccccccccaaaaccaaaaaaaaaaaaaaaaaaccaacccccccccccccccccccccccccccccccccaaaacccaaaaaccaaacccccciiinnnnnttxxxxxyyyyvvqqqllccccccccc",
"abaaaacccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccaaaacccaaaaaacaaaccccciiinnnnttttxxxxxyyyyvvqqmmmccccccccc",
"abaaaaccccccccaaaaacccaaaaacaaaaaacaaaaaaccccccccccccccccaaccccccccccccccccaacccccccaaaaaaaaaaciiinnnnttttxxxxxyyyyvvqqqmmmccccccccc",
"SbaaaacccccccaaaaaccccaaaaaccaaaaaaaaaaaccccccccccccccccaaacaacccccccccccccccccccccccaaaaaaaaachhhnnntttxxxEzzzzyyvvvqqqmmmccccccccc",
"abaaaacccccccaacaacccccaaaaaaaacaaaaaaaaaccccccccccccccccaaaaaccccccccccccccccccccccccaaaaaaacchhhnnntttxxxxxyyyyyyvvvqqmmmdddcccccc",
"abaaaacccccccccccccccccccaaaaaacaaaaaaaaaacccccccccccccaaaaaaccccccccaaaccccccccccccccaaaaaaccchhhnnntttxxxxywyyyyyyvvvqqmmmdddccccc",
"abaacccccccccccccccccccaaaaaaacccccaaaaaaacccccccccccccaaaaaaaacccccaaaacccccccccccccaaaaaaacaahhhmmmttttxxwwyyyyyyyvvvqqmmmdddccccc",
"abcccccccccccccccccccccaaaaaaacaaccaaacccccccccccccccccaacaaaaacccccaaaacccccccccccccaaacaaaaaahhhmmmmtsssswwyywwwwvvvvqqqmmdddccccc",
"abcccccccccccccccaaaccccaaaaaaaaaacaaccaaccccccccccccccccaaacaccccccaaaacccccccccccccccccaaaaacahhhmmmmmsssswwywwwwwvvrrqqmmdddccccc",
"abcccccccccccccaaaaaaccccaaaaaaaaaccaaaacccccccccccccccccaacccccccccccccccccccccccaaaccccaaaaaaahhhhhmmmmssswwwwwrrrrrrrrmmmmddccccc",
"abcccccccccccccaaaaaaccccaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccaaaaaacccccaaaaachhhhhmmmmsswwwwrrrrrrrrrkkmdddccccc",
"abccccccccccccccaaaaaccccccaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccaaaaaaccccaaaaacccchhggmmmssswwrrrrrkkkkkkkkdddacccc",
"abccaaaacccccccaaaaacccccccccaaaaaacaaaaacccccccccccccccccccccccccccccccccccccccaaaaaaccccaacaaaccccggggmmsssssrrlkkkkkkkkkdddaccccc",
"abccaaaacccccccaaaaacccccccccaaaaaaccccaacccccccccccccccccccccccccccccccccccccccaaaaaccccccccaaccccccgggmllssssrllkkkkkkkeeeddaccccc",
"abccaaaacccccccaaacccccccccccaaaaaacccccccccccccccccccaacccccccccccccccccccccccaaaaaacccccccccccccccccggllllssslllkkeeeeeeeeeaaacccc",
"abcccaaccccccccaaacaaaccccccaaaaaaaaaaacccccccccccccaaaaaacccccccccccccccccccccaaacaaacccccaacccccccccggglllllllllfeeeeeeeeaaaaacccc",
"abccccccccccaaaaaaaaaaccccccccccccaccaaaccacccccccccaaaaaaccccaaccaacccaaccccccaaaaaaacccccaaccccccccccggglllllllfffeeecccaaaaaacccc",
"abccccccccccaaaaaaaaacccccccccccccccaaaaaaaccccccccccaaaaaccccaaaaaacccaaaaaaccaaaaaacccaaaaaaaacccccccggggllllfffffccccccaacccccccc",
"abcccccccccccaaaaaaacccccccccccccccccaaaaaaccaacccccaaaaaccccccaaaaacccaaaaaacaaaaaaacccaaaaaaaaccccccccgggffffffffccccccccccccccccc",
"abccccccccccccaaaaaaacccccccccccccaaaaaaaaacaaaaccccaaaaacaaaaaaaaaacaaaaaaacaaaaaaaaaccccaaaacccccccccccggffffffacccccccccccccccaaa",
"abccccccccccccaaaaaaacaaccccccccccaaaaaaaaacaaaacccccaaaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaacccaaaaacccccccccccaffffaaaaccccccccccccccaaa",
"abccccccccccccaaacaaaaaacccccccccccaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaacaaaaaaacccaaacaaaccaaaaaacccccccccccccccccaaaccccccccccccccaaa",
"abccccccccccccaaccaaaaaccccccccccccccaaaaaaaccccaaaaaaaaaaaaccccaacccccaaaaaacccaaaccccccaaccaacccccccccccccccccaaacccccccccccaaaaaa",
"abcccccccccccccccaaaaaaaaccccccccccccaacccacccccccaaaaaaaaaaccccaacccccaaccccccccaccccccccccccccccccccccccccccccccccccccccccccaaaaaa",
]
input = realInput

print("input: " + str(input))
nodes = []
start = ""
end = ""


def calcnodeid(i,j):
    return str(i)+","+str(j)


print("initiating graph builder")
for (i,s) in enumerate(input):
    print("row done "+str(i))
    for (j,c) in enumerate(s.strip()):
        nodes.append(calcnodeid(i,j))
init_graph = {}

 
for node in nodes:
    init_graph[node] = {}

print("done scaffolding graph builder")
for (i,s) in enumerate(input):
    print("row done "+str(i))
    for (j,c) in enumerate(s.strip()):
        
        nodeid = calcnodeid(i,j)
        # print("--- "+nodeid+" ---")
        val = c
        if c == "S":
            val = "a"
            start = nodeid
        elif c == "E":
            val = "z"
            end = nodeid
        val = ordOfNode(c)


        if  j == 0:
            if ordOfNode(input[i][j+1]) == val+1 or ordOfNode(input[i][j+1]) <= val:
                # print(nodeid + " > " + calcnodeid(i,j+1) + "|" + str(input[i][j+1]) + " / " + c + " b1 " + str(ordOfNode(input[i][j+1]) == val+1) + " b2 " + str(ordOfNode(input[i][j+1]) <= val))
                init_graph[nodeid][calcnodeid(i,j+1)] = 1
        elif j == len(s.strip())-1:
            if ordOfNode(input[i][j-1]) == val+1 or ordOfNode(input[i][j-1]) <= val:
                # print(nodeid + " < " + calcnodeid(i,j-1) + "|" + str(input[i][j-1]) + " / " + c + " b1 " + str(ordOfNode(input[i][j-1]) == val+1) + " b2 " + str(ordOfNode(input[i][j-1]) <= val))
                init_graph[nodeid][calcnodeid(i,j-1)] = 1
        elif j > 0 and j < len(s.strip())-1 :
            if ordOfNode(input[i][j+1]) == val+1 or ordOfNode(input[i][j+1]) <= val:
                # print(nodeid + " > " + calcnodeid(i,j+1) + "|" + str(input[i][j+1]) + " / " + c + " b1 " + str(ordOfNode(input[i][j+1]) == val+1) + " b2 " + str(ordOfNode(input[i][j+1]) <= val))
                init_graph[nodeid][calcnodeid(i,j+1)] = 1
            if ordOfNode(input[i][j-1]) == val+1 or ordOfNode(input[i][j-1]) <= val:
                # print(nodeid + " < " + calcnodeid(i,j-1) + "|" + str(input[i][j-1]) + " / " + c + " b1 " + str(ordOfNode(input[i][j-1]) == val+1) + " b2 " + str(ordOfNode(input[i][j-1]) <= val))
                init_graph[nodeid][calcnodeid(i,j-1)] = 1

        if  i == 0:
            if ordOfNode(input[i+1][j]) == val+1 or ordOfNode(input[i+1][j]) <= val:
                # print(nodeid + " 5 v " + calcnodeid(i+1,j) + "|" + str(input[i+1][j]) + " / " + c + " b1 " + str(ordOfNode(input[i+1][j]) == val+1) + " b2 " + str(ordOfNode(input[i+1][j]) <= val))
                init_graph[nodeid][calcnodeid(i+1,j)] = 1
        elif i == len(input)-1:
            if ordOfNode(input[i-1][j]) == val+1 or ordOfNode(input[i-1][j]) <= val:
                # print(nodeid + " 6 ^ " + calcnodeid(i-1,j) + "|" + str(input[i-1][j]) + " / " + c + " b1 " + str(ordOfNode(input[i-1][j]) == val+1) + " b2 " + str(ordOfNode(input[i-1][j]) <= val))
                init_graph[nodeid][calcnodeid(i-1,j)] = 1
        elif i < len(input)-1 and i > 0:
            if ordOfNode(input[i+1][j]) == val+1 or ordOfNode(input[i+1][j]) <= val:
                # print(nodeid + " 7 v " + calcnodeid(i+1,j) + "|" + str(input[i+1][j]) + " / " + c + " b1 " + str(ordOfNode(input[i+1][j]) == val+1) + " b2 " + str(ordOfNode(input[i+1][j])) + str(val))
                init_graph[nodeid][calcnodeid(i+1,j)] = 1
            if ordOfNode(input[i-1][j]) == val+1 or ordOfNode(input[i-1][j]) <= val:
                # print(nodeid + " 8 ^ " + calcnodeid(i-1,j) + "|" + str(input[i-1][j]) + " / " + c + " b1 " + str(ordOfNode(input[i-1][j]) == val+1) + " b2 " + str(ordOfNode(input[i-1][j]) <= val))
                init_graph[nodeid][calcnodeid(i-1,j)] = 1

print("Start is " + start)
print("End is " + end)
    
	
graph = Dijkstra( init_graph, start_vertex=start)

graph.dijkstra()

print("dijkstra done")

path = graph.build_path(end)
print('S ->', end + ':', path, len(path)-1)
