import time
import sys
import os
import re

import stomp

topic = "adventofcode.day10.part1"
EOMRev = False
globalClock = 0
initDelay = 20
incrementDelay = 40
signalStrengths = []
registers= {"x": 1}
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def delay(body):
    if str(body) == "noop":
        return 1
    return 2
def updateState(body, registers):
    if str(body).startswith("addx "):
        registers["x"] += int(body.split(' ')[1])

class MyListener(stomp.ConnectionListener):
    def on_error(self, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        global globalClock
        global initDelay
        global incrementDelay
        global signalStrengths
        global registers
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            for i in range(delay(message.body)):
                globalClock += 1
                if  globalClock == initDelay or (globalClock-initDelay) % incrementDelay == 0:
                    signalStrengths.append(globalClock*registers["x"])
                    val = registers["x"]
                if i == delay(message.body) -1:
                    updateState(message.body, registers)
hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener()) 
conn.connect(username, password, wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic, id=91, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    line = line.strip()
    conn.send(body=f"{line}" , destination=topic)
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
print(sum(signalStrengths))
conn.disconnect()
