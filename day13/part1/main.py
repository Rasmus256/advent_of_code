import time

import stomp
import json

topic = "adventofcode.day13.part1"
EOMRev = False

def in_right_order(left, right):
    print(f"starting processing {left} {type(left)}, {right} {type(right)}")
    if type(left) is int and type(right) is int:
        print("Left less than right! In order")
        return left < right
    elif type(left) is int:
        print("Left is int, but not right. Wrapping left.")
        return in_right_order([left], right)
    elif type(right) is int:
        print("Right is int, but not right. Wrapping right.")
        return in_right_order(left, [right])
    elif left is list and right is list:
        print("left and right are lists.")
        if len(left) == 0 and len(right) > 0:
            print("Left side ran out first! In order")
            return True
        elif len(left) > 0 and len(right) > 0:
            in_order = in_right_order(left[0], right[0])
            if type(in_order) is None:
                print("No determination - trying next")
                return in_right_order(left[1:], right[1:])
            elif in_order:
                print("Comparison bubbling up - True!")
                return True
            else:
                print("Comparison bubbling up - False!")
                return False
        elif len(left) > 0 and len(right) == 0:
            print("Right side ran out first! Not in order")
            return False
        elif len(left) == 0 and len(right) == 0:
            print("Unable to determine order, as both sides were empty!")
            return None
    else:
        print(f"failed to process {left} {type(left)}, {right} {type(right)}")
        raise RuntimeError("unable to handle error")

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
            left = json.loads(left)
            right = json.loads(right)
            print(f"l: {left}")
            print(f"r: {right}")
            print(f"order: {in_right_order(left, right)}")

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
        Msg = '\n'.join(Msg)
        conn.send(body=f"{Msg}" , destination=topic)
        Msg = []
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
conn.disconnect()
