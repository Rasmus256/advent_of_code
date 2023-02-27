import time

import stomp

topic = "adventofcode.day13.part1"
EOMRev = False

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            left =  message.body.split("\n")[0]
            right = message.body.split("\n")[1]
            print(f"l: {left}")
            print(f"r: {right}")

hosts = [('amq.default.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener()) 
conn.connect('admin', 'admin', wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic, id=131, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
Msg = []
for line in Lines:
    line = line.strip()
    Msg.append(line)
    if line.strip() == "":
        conn.send(body=f"{Msg}" , destination=topic)
        Msg = []
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
conn.disconnect()
