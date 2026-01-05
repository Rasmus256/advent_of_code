import time
import sys
import re

import stomp

countFromStart = {"Test": 0}
topic = "adventofcode.day9"

hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.connect(username, password, wait=True,headers = {'client-id': topic+"reader"} )

file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    line = line.strip()
    parts = line.split(' ')
    for x in range(int(parts[1])): 
      conn.send(body=f"{parts[0]}" , destination=topic)
conn.send(body="EOM", destination=topic)

conn.disconnect()
