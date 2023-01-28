import sys
import math
from dijkstar import Graph, find_path

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
start = ""
end = ""


def calcnodeid(i,j):
    return i*10000+j


print("initiating graph builder")
graph = Graph()
possibleStarts = []

for (i,s) in enumerate(input):
    for (j,c) in enumerate(s.strip()):
        if ordOfNode(calcnodeid(i,j) == ord("a"))
            possibleStarts.append(calcnodeid(i,j))

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
                graph.add_edge(nodeid,calcnodeid(i,j+1), 1)
        elif j == len(s.strip())-1:
            if ordOfNode(input[i][j-1]) == val+1 or ordOfNode(input[i][j-1]) <= val:
                # print(nodeid + " < " + calcnodeid(i,j-1) + "|" + str(input[i][j-1]) + " / " + c + " b1 " + str(ordOfNode(input[i][j-1]) == val+1) + " b2 " + str(ordOfNode(input[i][j-1]) <= val))
                graph.add_edge(nodeid,calcnodeid(i,j-1), 1)
        elif j > 0 and j < len(s.strip())-1 :
            if ordOfNode(input[i][j+1]) == val+1 or ordOfNode(input[i][j+1]) <= val:
                # print(nodeid + " > " + calcnodeid(i,j+1) + "|" + str(input[i][j+1]) + " / " + c + " b1 " + str(ordOfNode(input[i][j+1]) == val+1) + " b2 " + str(ordOfNode(input[i][j+1]) <= val))
                graph.add_edge(nodeid,calcnodeid(i,j+1), 1)
            if ordOfNode(input[i][j-1]) == val+1 or ordOfNode(input[i][j-1]) <= val:
                # print(nodeid + " < " + calcnodeid(i,j-1) + "|" + str(input[i][j-1]) + " / " + c + " b1 " + str(ordOfNode(input[i][j-1]) == val+1) + " b2 " + str(ordOfNode(input[i][j-1]) <= val))
                graph.add_edge(nodeid,calcnodeid(i,j-1), 1)

        if  i == 0:
            if ordOfNode(input[i+1][j]) == val+1 or ordOfNode(input[i+1][j]) <= val:
                # print(nodeid + " 5 v " + calcnodeid(i+1,j) + "|" + str(input[i+1][j]) + " / " + c + " b1 " + str(ordOfNode(input[i+1][j]) == val+1) + " b2 " + str(ordOfNode(input[i+1][j]) <= val))
                graph.add_edge(nodeid,calcnodeid(i+1,j), 1)
        elif i == len(input)-1:
            if ordOfNode(input[i-1][j]) == val+1 or ordOfNode(input[i-1][j]) <= val:
                # print(nodeid + " 6 ^ " + calcnodeid(i-1,j) + "|" + str(input[i-1][j]) + " / " + c + " b1 " + str(ordOfNode(input[i-1][j]) == val+1) + " b2 " + str(ordOfNode(input[i-1][j]) <= val))
                graph.add_edge(nodeid,calcnodeid(i-1,j), 1)
        elif i < len(input)-1 and i > 0:
            if ordOfNode(input[i+1][j]) == val+1 or ordOfNode(input[i+1][j]) <= val:
                # print(nodeid + " 7 v " + calcnodeid(i+1,j) + "|" + str(input[i+1][j]) + " / " + c + " b1 " + str(ordOfNode(input[i+1][j]) == val+1) + " b2 " + str(ordOfNode(input[i+1][j])) + str(val))
                graph.add_edge(nodeid,calcnodeid(i+1,j), 1)
            if ordOfNode(input[i-1][j]) == val+1 or ordOfNode(input[i-1][j]) <= val:
                # print(nodeid + " 8 ^ " + calcnodeid(i-1,j) + "|" + str(input[i-1][j]) + " / " + c + " b1 " + str(ordOfNode(input[i-1][j]) == val+1) + " b2 " + str(ordOfNode(input[i-1][j]) <= val))
                graph.add_edge(nodeid,calcnodeid(i-1,j), 1)

print("Start is ", start)
print("End is ", end)

p = find_path(graph, start, end)
print(p.total_cost)
