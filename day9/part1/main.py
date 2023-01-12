import time
import sys
import re

import stomp

countFromStart = {"Test": 0}
topic = "adventofcode.day9.part1"
EOMRev = False

HeadPos = [0,0]
TailPos = [0,0]

TailPositions= []

def moveUp(element):
    element[1] += 1
def moveDown(element):
    element[1] -= 1
def moveRight(element):
    element[0] += 1
def moveLeft(element):
    element[0] -= 1

def updateTailPos(HeadPos, TailPos):
    
    if HeadPos[0] == TailPos[0]:
        # H
        # x
        # T
        if HeadPos[1] - TailPos[1] == 2:
            moveUp(TailPos)
        # T
        # x
        # H
        elif HeadPos[1] - TailPos[1] == -2:
            moveDown(TailPos)
    # y is the same
    elif HeadPos[1] == TailPos[1]:
        # T x H
        if HeadPos[0] - TailPos[0] == 2:
            moveRight(TailPos)
        # H x T
        elif HeadPos[0] - TailPos[0] == -2:
            moveLeft(TailPos)

    #Diagonals
    elif abs (HeadPos[0] - TailPos[0]) == 2:
        # H x x
        # x x T
        
        # x x H
        # T x x
        if HeadPos[1] - TailPos[1] == 1:
            moveUp(TailPos)
            updateTailPos(HeadPos, TailPos)
        # x x T
        # H x x

        # T x x
        # x x H
        elif HeadPos[1] - TailPos[1] == -1:
            moveDown(TailPos)
            updateTailPos(HeadPos, TailPos)
    elif abs (HeadPos[1] - TailPos[1]) == 2:
        # H x
        # x x
        # x T

        # x T
        # x x
        # H x
        if HeadPos[0] - TailPos[0] == -1:
            moveLeft(TailPos)
            updateTailPos(HeadPos, TailPos)
                
        # x H
        # x x
        # T x

        # T x
        # x x
        # x H
        elif HeadPos[0] - TailPos[0] == 1:
            moveRight(TailPos)
            updateTailPos(HeadPos, TailPos)


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        global HeadPos
        global TailPos
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            direction = message.body
            match direction:
                case 'R':
                    moveRight(HeadPos)
                case 'L':
                    moveLeft(HeadPos)
                case 'U':
                    moveUp(HeadPos)
                case 'D':
                    moveDown(HeadPos)
            updateTailPos(HeadPos, TailPos) 
            TailPositions.append(f"{TailPos[0]}|{TailPos[1]}")

hosts = [('amq.default.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic, id=91, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    line = line.strip()
    parts = line.split(' ')
    for x in range(int(parts[1])):
      conn.send(body=f"{parts[0]}" , destination=topic)
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
print(len(set(TailPositions)))

conn.disconnect()
