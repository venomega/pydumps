import sys
import threading
import os


ip = sys.argv[1]
token = ip[::-1]
gold_number = token.index(".")

if ip.count(".") != 3:
    print ("error, argument provided is not an ipv4 addreess")
    exit(1)



def do(*list):
    buff = ""
    for element in list:
        buff += element

    data = os.popen(f"ping -c 1 -W 1 {buff}").read()
    if "ttl" in data:
        print (buff)
 
        

for i in range(255):
    threading.Thread(target=do,args=f"{ip[:-gold_number]}{i}").start()


