import time
import sys
import re

import stomp
import os
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

countFromStart = {"Test": 0}

EOMRev = False

def allDifferent(input):
  return len(''.join(set(input))) == 4

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        global countFromStart
        if message.body == "EOM":
            global EOMRev 
            EOMRev = True
        elif message.body.startswith("EOL|"):
            spl = message.body.split("|")
            print(spl[1] + "|"+str(countFromStart[spl[1]]+4))
        else:
            offsetAndContent = message.body.split('|')
            if offsetAndContent[2] not in countFromStart:
                countFromStart[offsetAndContent[2]] = 0
            if countFromStart[offsetAndContent[2]] == 0 or int(offsetAndContent[0]) < countFromStart[offsetAndContent[2]]:
              #print("Considering " + message.body + " vs " + str(countFromStart[offsetAndContent[2]]))
              if allDifferent(offsetAndContent[1]):
                countFromStart[offsetAndContent[2]] = int(offsetAndContent[0])

hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect(username, password, wait=True,headers = {'client-id': 'day6_part1'} )
conn.subscribe(destination='adventofcode.day6.part1::adventofcode.day6.part1', id=61, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})

file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    line = line.strip()
    for x in range(len(line)-3):
      substr= line[x:x+4:]
      conn.send(body=f"{x}|{substr}|{line}" , destination='adventofcode.day6.part1')
    conn.send(body=f"EOL|{line}", destination='adventofcode.day6.part1')
conn.send(body="EOM", destination='adventofcode.day6.part1')
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)

conn.disconnect()
