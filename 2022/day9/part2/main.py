import time
import sys
import re

import stomp
import os
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

countFromStart = {"Test": 0}
topic = "adventofcode.day9.part2"
EOMRev = False

HeadPos = [0,0]
_1Pos = [0,0]
_2Pos = [0,0]
_3Pos = [0,0]
_4Pos = [0,0]
_5Pos = [0,0]
_6Pos = [0,0]
_7Pos = [0,0]
_8Pos = [0,0]
TailPos = [0,0]

TailPositions= []

def checkForBrokenChains(Front, Back):
    global TailPositions
    if abs(Front[0] - Back[0]) + abs(Front[1] - Back[1]) > 4:
        print(f"{Front}, {Back}")

def moveUp(element):
    element[1] += 1
def moveDown(element):
    element[1] -= 1
def moveRight(element):
    element[0] += 1
def moveLeft(element):
    element[0] -= 1

def handleCardinalUpdates(Front, Back):
    if Front[0] == Back[0]:
        # print(f"Handling Vertical move {Front} {Back}")
        # H
        # x
        # T
        if Front[1] - Back[1] == 2:
            moveUp(Back)
        # T
        # x
        # H
        elif Front[1] - Back[1] == -2:
            moveDown(Back)
        # print(f"Vertical move Res {Front} {Back}")
    # y is the same
    elif Front[1] == Back[1]:
        # print(f"Handling Horizontal move {Front} {Back}")
        # T x H
        if Front[0] - Back[0] == 2:
            moveRight(Back)
        # H x T
        elif Front[0] - Back[0] == -2:
            moveLeft(Back)
        # print(f"Horizontal move Res {Front} {Back}")
    else:
        # print(f"Cardinal called - covers {Front} {Back}")
        global TailPositions
        if abs(Front[0] - Back[0]) + abs(Front[1] - Back[1]) > 2:
            print(f"Not a valid cardinal move {Front} {Back}")

def handleDiagonalUpdates(Front, Back):
    if abs (Front[0] - Back[0]) == 2 and abs (Front[1] - Back[1]) == 2 :
        # print(f"Handling double diagonal {Front} {Back}")
        # x x H
        # x x x
        # T x x

        # H x x
        # x x x
        # x x T
        if Front[1] - Back[1] == 2:
            # print(f"Case 1 {Front} {Back}")
            moveUp(Back)
            # print(f"Res 1 {Front} {Back}")
        # x x T
        # x x x
        # H x x

        # T x x
        # x x x
        # x x H
        elif Front[1] - Back[1] == -2:
            # print(f"Case 2 {Front} {Back}")
            moveDown(Back)
            # print(f"Res 2 {Front} {Back}")
        if Front[0] - Back[0] == -2:
            # print(f"Case A {Front} {Back}")
            moveLeft(Back)
            # print(f"Res A {Front} {Back}")
        elif Front[0] - Back[0] == 2:
            # print(f"Case B {Front} {Back}")
            moveRight(Back)
            # print(f"Res B {Front} {Back}")
    elif abs (Front[0] - Back[0]) == 2 and abs(Front[1] - Back[1]) == 1:
        # print(f"Handling simple diagonal 1 {Front} {Back}")
        # H x x
        # x x T
        
        # x x H
        # T x x
        if Front[1] - Back[1] == 1:
            # print(f"Case 1 {Front} {Back}")
            moveUp(Back)
            # print(f"Tmp 1 {Front} {Back}")
            handleCardinalUpdates(Front, Back)
            # print(f"Res 1 {Front} {Back}")
        # x x T
        # H x x

        # T x x
        # x x H
        elif Front[1] - Back[1] == -1:
            # print(f"Case 2 {Front} {Back}")
            moveDown(Back)
            # print(f"Tmp 2 {Front} {Back}")
            handleCardinalUpdates(Front, Back)
            # print(f"Res 2 {Front} {Back}")
    elif abs (Front[1] - Back[1]) == 2 and abs(Front[0] - Back[0]) == 1:
        # print(f"Handling simple diagonal 2 {Front} {Back}")
        # H x
        # x x
        # x T

        # x T
        # x x
        # H x
        if Front[0] - Back[0] == -1:
            moveLeft(Back)
            handleCardinalUpdates(Front, Back)
                
        # x H
        # x x
        # T x

        # T x
        # x x
        # x H
        elif Front[0] - Back[0] == 1:
            moveRight(Back)
            handleCardinalUpdates(Front, Back)
    else:
        # print(f"Diagonal called - no action needed {Front} {Back}")
        if abs(Front[0] - Back[0]) + abs(Front[1] - Back[1]) > 4:
            print(f"Not a valid diagonal move {Front} {Back}")
            repr(Front)


def updateTailPos(Front, Back):
    if Front[0] == Back[0] or Front[1] == Back[1] :
        handleCardinalUpdates(Front, Back)
    #Diagonals
    else:
        handleDiagonalUpdates(Front, Back)
    checkForBrokenChains(Front, Back)

###
# T x x
# x x x
# x x x
# x x H
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
            # print(f"---{direction}---")
            match direction:
                case 'R':
                    moveRight(HeadPos)
                case 'L':
                    moveLeft(HeadPos)
                case 'U':
                    moveUp(HeadPos)
                case 'D': 
                    moveDown(HeadPos)
            # print(f"  ---1---")
            updateTailPos(HeadPos, _1Pos)
            # print(f"  ---Tail---")
            updateTailPos(_1Pos, _2Pos)
            updateTailPos(_2Pos, _3Pos)
            updateTailPos(_3Pos, _4Pos)
            updateTailPos(_4Pos, _5Pos)
            updateTailPos(_5Pos, _6Pos)
            updateTailPos(_6Pos, _7Pos)
            updateTailPos(_7Pos, _8Pos)
            updateTailPos(_8Pos, TailPos)
            

            TailPositions.append(f"{TailPos[0]}|{TailPos[1]}")

hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect(username, password, wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic+"::"+topic, id=92, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
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
