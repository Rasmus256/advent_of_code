import time
import sys
import re

import stomp

piles = {
'1':['C','Z','N','B','M','W','Q','V'],
'2':['H','Z','R','W','C','B'],
'3':['F','Q','R','J'],
'4':['Z','S','W','H','F','N','M','T'],
'5':['G','F','W','L','N','Q','P'],
'6':['L','P','W'],
'7':['V','B','D','R','G','C','Q','J'],
'8':['Z','Q','N','B','W'],
'9':['H','L','F','C','G','T','J']
}

EOMRev = False
class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, message):
        if message.body == "EOM":
            global EOMRev
            EOMRev = True
        else:
            global piles
            fromTo = message.body.split('|')
            piles[fromTo[1]].append(piles[fromTo[0]].pop())



hosts = [('amq', 61613)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True,headers = {'client-id': 'day5_part1'} )
conn.subscribe(destination='adventofcode.day5.part1', id=51, ack='auto',headers = {'subscription-type': 'MULTICAST','durable-subscription-name':'someValue'})

file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
for line in Lines:
    nums = re.findall(r'\d+', line.strip())
    for x in range(int(nums[0])):
      conn.send(body=f"{nums[1]}|{nums[2]}" , destination='adventofcode.day5.part1')
conn.send(body="EOM", destination='adventofcode.day5.part1')
while not EOMRev:
    print("Wating for EOM")
    time.sleep(1)
print(
  piles['1'].pop()+
  piles['2'].pop()+
  piles['3'].pop()+
  piles['4'].pop()+
  piles['5'].pop()+
  piles['6'].pop()+
  piles['7'].pop()+
  piles['8'].pop()+
  piles['9'].pop()
)

conn.disconnect()