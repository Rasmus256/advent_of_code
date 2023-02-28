import time

import stomp

topic = "adventofcode.day14.part1"
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

hosts = [('amq.default.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener()) 
conn.connect('admin', 'admin', wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic, id=131, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    line = line.strip()
    segments = line.split(' -> ')
    if len(segments) == 1:
        print(segments[0])
    for i in range(1,len(segments)):
        print(f"{segments[i-1]} -> {segments[i]}")
        startcoords = segments[i-1].split(",")
        endcoords   = segments[i].split(",")
        msg = {x0: startcoords[0],y0: startcoords[1],
        x1: endcoords[0],y1: endcoords[1]}
    conn.send(body=json.dumps(msg) , destination=topic)
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
conn.disconnect()
