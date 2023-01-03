import time
import sys

import stomp

hosts = [('amq.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.connect('admin', 'admin', wait=True,headers = {'client-id': 'clientname_reader'} )

file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
count = 0
for line in Lines:
    if line != "\n":
        count += int(line.strip())
    else:
        conn.send(body=str(count), destination='adventofcode.day1')
        count=0

conn.send(body="EOM", destination='adventofcode.day1')

conn.disconnect()