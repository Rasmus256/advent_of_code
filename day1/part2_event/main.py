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

hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True,headers = {'client-id': 'day2_part2'} )
conn.subscribe(destination='adventofcode.day1', id=2, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})

while not EOMRev: 
    print("Waiting for EOM")
    time.sleep(1)

results.sort(reverse=True)
print(results[:3])

conn.disconnect()
