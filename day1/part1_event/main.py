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

hosts = [('amq.default.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True,headers = {'client-id': 'clientname'} )
conn.subscribe(destination='adventofcode.day1', id=1, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})

while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
print(result)

conn.disconnect()