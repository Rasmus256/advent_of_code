import time
import sys
import re

import stomp

topic = "adventofcode.day10.part2"
EOMRev = False
globalClock = 0
TMPOut = []
CRTOut= [[],[],[],[],[],[]]
registers= {"x": 1}

def delay(body):
    if str(body) == "noop":
        return 1
    return 2
def updateState(body, registers):
    print("Updating")
    if str(body).startswith("addx "):
        registers["x"] += int(body.split(' ')[1])
        print(registers)

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        global globalClock
        global registers
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            for i in range(delay(message.body)):
                globalClock += 1
                val = registers["x"]%40
                rawreg = registers["x"]
                print(f"{rawreg} - {val}")
                s = "*"
                if val >= ((globalClock-1)%40) -1 and val <= ((globalClock-1)%40 +1):
                    s = "#"
                TMPOut.append(s)
                if i == delay(message.body) -1:
                    updateState(message.body, registers)

hosts = [('amq.default.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True,headers = {'client-id': topic} )
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

CRTOut[0] = TMPOut[0:40]
CRTOut[1] = TMPOut[40:80]
CRTOut[2] = TMPOut[80:120]
CRTOut[3] = TMPOut[120:160]
CRTOut[4] = TMPOut[160:200]
CRTOut[5] = TMPOut[200:240]

for line in CRTOut:
    print(''.join(line))
conn.disconnect()
