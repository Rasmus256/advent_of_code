import time
import sys

import stomp


result=0
EOMRev = False
class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            global result
            result = max(result,int(message.body))



hosts = [('amq', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True,headers = {'client-id': 'clientname'} )
conn.subscribe(destination='adventofcode.day1.part1', id=1, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})

file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
count = 0
for line in Lines:
    if line != "\n":
        count += int(line.strip())
    else:
        conn.send(body=str(count), destination='adventofcode.day1.part1')
        count=0

conn.send(body="EOM", destination='adventofcode.day1.part1')
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
print(result)

conn.disconnect()