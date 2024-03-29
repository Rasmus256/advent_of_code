import time

import stomp
import os
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
import json

topic = "adventofcode.day13.part2"
EOMRev = False

packets = []

def in_right_order(left, right):
    # print(f"starting processing {left} {type(left)}, {right} {type(right)}")
    if type(left) is int and type(right) is int:
        if left == right:
            # print("Left equal to right! No determination")
            return None
        elif left < right:
            # print("Left less than right! In order")
            return True
        else:
            # print("Right less than left! Not in order")
            return False
        # print("Left less than right! In order")
        return left < right
    elif type(left) is int:
        # print("Left is int, but not right. Wrapping left.")
        return in_right_order([left], right)
    elif type(right) is int:
        # print("Right is int, but not right. Wrapping right.")
        return in_right_order(left, [right])
    elif type(left) is list and type(right) is list:
        # print("left and right are lists.")
        if len(left) == 0 and len(right) > 0:
            # print("Left side ran out first! In order")
            return True
        elif len(left) > 0 and len(right) > 0:
            in_order = in_right_order(left[0], right[0])
            if in_order == None:
                # print("No determination - trying next")
                return in_right_order(left[1:], right[1:])
            elif in_order:
                # print("Comparison bubbling up - True!")
                return True
            else:
                # print("Comparison bubbling up - False!")
                return False
        elif len(left) > 0 and len(right) == 0:
            # print("Right side ran out first! Not in order")
            return False
        elif len(left) == 0 and len(right) == 0:
            # print("Unable to determine order, as both sides were empty!")
            return None
    else:
        # print(f"failed to process {left} {type(left)}, {right} {type(right)}")
        raise RuntimeError("unable to handle error")
class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        # print("-----------  --------   ------------   ----------")
        
        global packets
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
            idx = []
            for i, p in enumerate(packets):
                if p == [[2]] or p == [[6]]:
                    print(f"Hit {p} at {i+1}")
        else:
            Message = json.loads(message.body)
            left =  Message["left"]
            inserted= False
            for idx, right in enumerate(packets):
                if in_right_order(left, right):
                    # print(f"inserting {left} between {packets[:idx]} and {packets[idx:]}")
                    tmp = []
                    for p in packets[:idx]:
                        tmp.append(p)
                    tmp.append(left)
                    for p in packets[idx:]:
                        tmp.append(p)
                    packets = tmp
                    # print(f"{message.body} is in right order against {right}!  {Message['index']}" )

                    inserted=True
                    break
                # else:
                    # print(f"{message.body} is not in right order against {right}! Try the next index!" )
            if not inserted:
                packets.append(left)
            # print(f"{packets}")

hosts = [('amq-hdls-svc.adventofcode.svc.cluster.local', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener()) 
conn.connect(username, password, wait=True,headers = {'client-id': topic} )
conn.subscribe(destination=topic+"::"+topic, id=132, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})
file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
msg = {}
idx = 0
for line in Lines:
    line = line.strip()
    if not line == "":
        msg = {}
        r = line.strip()
        idx = idx+1
        msg['index'] = idx
        msg['left'] = json.loads(line)
        # print(json.dumps(msg))
        conn.send(body=json.dumps(msg) , destination=topic)
conn.send(body="EOM", destination=topic)
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
conn.disconnect()
