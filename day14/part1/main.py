import time

import stomp
import json

topic = "adventofcode.day14.part1"
EOMRev = False
RocksDone = False
EquivalenceReached = False
rocks = {}
class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        global RocksDone
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        elif message.body == "ROCKSDONE":
            RocksDone = True
        elif not RocksDone:
            rock = json.loads(message.body)
            y = int(rock['y'])
            x = int(rock['x'])
            if not y in rocks:
                rocks[y] = []
            rocks[y].append(x)
        else:
            print(f"Sand spawned at {message.body}")

hosts = [('amq.default.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener()) 
conn.connect('admin', 'admin', wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic, id=131, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
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
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
print(rocks)
for row in rocks:
    rowString = ""
    for i in range(494,504):
        if i in rocks[row]:
            rowString = rowString + "X"
        else:
            rowString = rowString + "*"
    print(rowString)
conn.disconnect()
