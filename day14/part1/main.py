import time

import stomp
import os
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
import json

topic = "adventofcode.day14.part1"
EOMRev = False
RocksDone = False
EquivalenceReached = False
rocks = {}
sand = {}
maxSands = 999999

def countSands(sand):
    i = 0
    for s in sand:
        i = i + len(sand[s])

    return i

def getMinRock(rocks):
    i = 0
    for s in rocks:
        i = min(i, min(rocks[s]))
    return i

def getMaxRock(rocks):
    i = 0
    for s in rocks:
        i = max(i, max(rocks[s]))
    return i

class MyListener(stomp.ConnectionListener):
    def on_error(self, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        global RocksDone
        if message.body == "ROCKSDONE":
            RocksDone = True
        elif not RocksDone:
            rock = json.loads(message.body)
            y = int(rock['y'])
            x = int(rock['x'])
            if not y in rocks:
                rocks[y] = []
            rocks[y].append(x)
        else:
            print(f"Processing sand for {message.body}")
            newSand = json.loads(message.body)
            newSand = simulateSand(rocks, sand, newSand)
            y = int(newSand['y'])
            x = int(newSand['x'])
            global EquivalenceReached
            global maxSands
            if y > max(rocks):
                EquivalenceReached = True
            else:
                if not y in sand:
                    sand[y] = []
                if not x in sand[y]:
                    sand[y].append(x)
            numSands = countSands(sand)
            print(numSands)
            EquivalenceReached = EquivalenceReached or maxSands < numSands
            if not EquivalenceReached:
                global conn
                conn.send(body=json.dumps({'x':500, 'y':0}), destination=topic)
            else:
                global EOMRev
                EOMRev = True

def prettyPrint(rocks, sand):
    for row in range(0,max(rocks)+1):
        rowString = f"{row}: "
        for i in range(getMinRock(rocks),getMaxRock(rocks)):
            if row in rocks and i in rocks[row]:
                rowString = rowString + "#"
            elif row in sand and i in sand[row]:
                rowString = rowString + "o"
            else:
                rowString = rowString + "*"
        print(rowString)

def checkIfFree(rocks, sand, newPosition):
    return not ((newPosition['y'] in rocks and newPosition['x'] in rocks[newPosition['y']]) or (newPosition['y'] in sand and newPosition['x'] in sand[newPosition['y']]))

def simulateSand(rocks, sand, newSand):
    y = int(newSand['y'])
    x = int(newSand['x'])
    if y > max(rocks):
        return newSand
    # Try to fall down
    newPosition= {'x': x, 'y': y+1}
    if checkIfFree(rocks, sand, newPosition):
        return simulateSand(rocks, sand, newPosition)
    # Try to fall down left
    newPosition= {'x': x-1, 'y': y+1}
    if checkIfFree(rocks, sand, newPosition):
        return simulateSand(rocks, sand, newPosition)
    # Try to fall down right
    newPosition= {'x': x+1, 'y': y+1}
    if checkIfFree(rocks, sand, newPosition):
        return simulateSand(rocks, sand, newPosition)
    # Default stay where it was
    return newSand


hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect(username, password, wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic+'::'+topic, id=141, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    line = line.strip()
    segments = line.split(' -> ')
    if len(segments) == 1:
        startcoords = segments[0].split(",")
        msg = {'x': int(startcoords[0]),'y': int(startcoords[1])}
        conn.send(body=json.dumps(msg) , destination=topic)
    for i in range(1,len(segments)):
        startcoords = segments[i-1].split(",")
        endcoords   = segments[i].split(",")
        if startcoords[0] == endcoords[0] : #vertical line
            for y in range(min(int(startcoords[1]), int(endcoords[1])),max(int(startcoords[1]), int(endcoords[1]) )) :
                msg = {'x': int(startcoords[0]),'y': y}
                conn.send(body=json.dumps(msg) , destination=topic)
            msg = {'x': int(endcoords[0]),'y': endcoords[1]}
            conn.send(body=json.dumps(msg) , destination=topic)
            msg = {'x': int(startcoords[0]),'y': startcoords[1]}
            conn.send(body=json.dumps(msg) , destination=topic)
        else: #horizontal line
            for x in range(min(int(startcoords[0]), int(endcoords[0])),max(int(startcoords[0]), int(endcoords[0]) )) :
                msg = {'x': x,'y': int(startcoords[1])}
                conn.send(body=json.dumps(msg) , destination=topic)
            msg = {'x': int(endcoords[0]),'y': endcoords[1]}
            conn.send(body=json.dumps(msg) , destination=topic)
            msg = {'x': int(startcoords[0]),'y': startcoords[1]}
            conn.send(body=json.dumps(msg) , destination=topic)

conn.send(body="ROCKSDONE", destination=topic)
conn.send(body=json.dumps({'x':500, 'y':0}), destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
prettyPrint(rocks, sand)
conn.disconnect()
