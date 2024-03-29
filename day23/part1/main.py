import time

import stomp
import os
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

topic = "adventofcode.day23.part1"
EOMRev = False

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            print(f"{message.body}")

hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener()) 
conn.connect(username, password, wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic+"::"+topic, id=131, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    line = line.strip()
    conn.send(body=f"{line}" , destination=topic)
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
conn.disconnect()
