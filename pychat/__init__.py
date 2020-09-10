import net
import sys
import os
import time
import storage


PID=os.getpid() 


class commands():
    d = {"NICK":"","MSG":"","VERSION":""}

        
class order():
    def __init__(self,client_object,addr):
        self.co = client_object
        self.addr = addr
        self.first_time()
    def first_time(self)
        data = self.co.recv(1080).decode().split()
        if data[0] in commands().d.keys():
            storage.put_nick(data[0],self.addr)

        
s =net.Server()

while True:
    #get client connection
    client_object, address = s.accept()
    os.fork()
    if os.getpid() ==PID:
        continue
    order(client_object,address)    #make something with client
    exit(0)
