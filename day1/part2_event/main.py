import time
import sys

import stomp


results=[]
EOMRev = False
class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            global results
            results.append(int(message.body))



hosts = [('amq', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True,headers = {'client-id': 'day2_part2'} )
conn.subscribe(destination='adventofcode.day1.part2', id=2, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})

file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
count = 0
for line in Lines:
    if line != "\n":
        count += int(line.strip())
    else:
        conn.send(body=str(count), destination='adventofcode.day1.part2')
        count=0
conn.send(body="EOM", destination='adventofcode.day1.part2')
while not EOMRev: 
    print("Waiting for EOM")
    time.sleep(1)

results.sort(reverse=True)
print(results[:3])

conn.disconnect()