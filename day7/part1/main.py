import time
import sys
import re

import stomp

fs = {}
currentDir = {}
upDir
topic = "adventofcode.day7.part1"
EOMRev = False

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        global countFromStart
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            if message.command == 'cd /':
                currentDir = fs
            elif message.command.startswith('cd'):
                print('switching dir to')
            print(message)

hosts = [('amq', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic, id=61, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})

file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
currentCommand = {'sent':False}
for line in Lines:
    if line.startswith('$'):
        if 'command' in currentCommand:
            conn.send(body=currentCommand['result'], command = currentCommand['command'], result = currentCommand['result'], destination=topic)
            currentCommand['sent']=True
        currentCommand['command'] = line.strip().replace('$ ','')
        currentCommand['result'] = []
        currentCommand['sent']=False
    else:
        if 'result' not in currentCommand:
            currentCommand['result'] = []
        currentCommand['result'].append(line.strip())
if not currentCommand['sent']:
    conn.send(body='|'.join(currentCommand['result']), command = currentCommand['command'], result = currentCommand['result'], destination=topic)
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)

conn.disconnect()