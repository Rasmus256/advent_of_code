import time

import stomp
import os
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
import json

topic = "adventofcode.day13.part1"
EOMRev = False
Result = 0

def in_right_order(left, right):
    print(f"starting processing {left} {type(left)}, {right} {type(right)}")
    if type(left) is int and type(right) is int:
        if left == right:
            print("Left equal to right! No determination")
            return None
        elif left < right:
            print("Left less than right! In order")
            return True
        else:
            print("Right less than left! Not in order")
            return False
        print("Left less than right! In order")
        return left < right
    elif type(left) is int:
        print("Left is int, but not right. Wrapping left.")
        return in_right_order([left], right)
    elif type(right) is int:
        print("Right is int, but not right. Wrapping right.")
        return in_right_order(left, [right])
    elif type(left) is list and type(right) is list:
        print("left and right are lists.")
        if len(left) == 0 and len(right) > 0:
            print("Left side ran out first! In order")
            return True
        elif len(left) > 0 and len(right) > 0:
            in_order = in_right_order(left[0], right[0])
            if in_order == None:
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
        global Result
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
            print(f"res: {Result}")
        else:
            Message = json.loads(message.body)
            left =  Message["left"]
            right = Message["right"]
            if in_right_order(left, right):
                print(f"{message.body} is in right order! {Result} {Message['index']}" )
                Result = Result + Message['index']
            else:
                print(f"{message.body} is not in right order!" )

hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener()) 
conn.connect(username, password, wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic+"::"+topic, id=131, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
msg = {}
idx = 0
for line in Lines:
    line = line.strip()
    if line == "":
        r = line.strip()
        idx = idx+1
        msg['index'] = idx
        print(json.dumps(msg))
        conn.send(body=json.dumps(msg) , destination=topic)
        msg = {}
    elif not 'left' in msg:
        msg['left'] = json.loads(line)
    else: 
        msg['right'] = json.loads(line)
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
conn.disconnect()
