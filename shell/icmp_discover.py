import sys
import threading
import os


def do(*list):
    buff = ""
    for element in list:
        buff += element

    data = os.popen(f"ping -c 1 -W 1 {buff}").read()
    if "ttl" in data:
        print (buff)
 

ip = sys.argv[1]
token = ip[::-1]
gold_number = token.index(".")


for i in range(255):
    threading.Thread(target=do,args=f"{ip[:-gold_number]}{i}").start()


