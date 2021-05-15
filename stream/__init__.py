#!/usr/bin/env python3

import socket
import sys
import os
import ifaddr
from threading import Thread as t

def help():
        print ("USAGE:\n <syntax>\n program <option> <ip address> </file/to/send>\n\n<options>\n send\nrecv", file=sys.stderr)
        exit(1)

class stream(object):
        """
        This library is a simple way to send and receive files in a specific port(33333)
        
        EXAMPLE 1:
        
        peer 1   <=   ip: 1.1.1.1
        >>> s = stream()
        >>> s.serv_send("./file/to/send")
        
        peer 2  <= ip 1.1.1.2
        >>> s = steam()
        >>> s.connect_recv("1.1.1.1", "./file/to/recv")
        
        `peer 1` and `peer 2` are two users running this same library
        `peer 1` await for an incoming connection and send the file to `peer 2`
        
        """

        
        def connect_send(self,ip,filename):
                """
                connect to an specific ip and send given file
                two values are type str
                """
                s = socket.socket()
                print ("sending %s" %(filename))
                s.connect((ip,33333))
                fd=open(filename, "br")
                while True:
	                asd = fd.read(1080)
	                if not asd:
		                break
	                else:
		                s.send(asd)
                fd.close()
                
        def connect_recv(self,ip,filename):
                """
                connect to an specific ip and receive given file
                two values are type str
                """
                s = socket.socket()
                print ("sending %s" %(filename))
                s.connect((ip,33333))
                fd=open(filename, "bw")
                while True:
	                asd = s.recv(1080)
	                if not asd:
		                break
	                else:
		                fd.write(asd)
                fd.close()
                
        def serv_send(self,filename):
                """
                listen and wait for a certain client and send given file
                filename  are type str
                """
                
                s = socket.socket()
                s.bind(("0.0.0.0",33333))
                s.listen(1)
                sock, addr = s.accept()
                fd=open(filename, "br")
                while True:
	                asd = fd.read(1080)
	                if not asd:
		                break
	                else:
		                sock.send(asd)
                fd.close()

        def serv_recv(self,filename):
                """
                listen to and receive given file
                filename value are type str
                """
                s = socket.socket()
                s.bind(("0.0.0.0",33333))
                s.listen(1)
                sock, addr = s.accept()
                fd=open(filename, "bw")
                while True:
	                asd = sock.recv(1080)
	                if not asd:
		                break
	                else:
		                fd.write(asd)
                fd.close()

class Nick():
        def __init__(self, name, ip):
                self.name = name
                self.ip = ip

        
class discover():
        def __init__(self):
                self.nick = []
                self.look()

        def _get_ip(self):
                self.ips = []
                for ifname in self.ifname:
                        if ifname.name == 'lo':
                                continue
                        for ip in ifname.ips:
                                if ip.ip.count('.') == 3:
                                        self.ips.append(ip.ip)

        def look(self):
                self.ifname = ifaddr.get_adapters()
                self._get_ip()
                for ip in self.ips:
                        _1, _2, _3, _4 = ip.split('.')
                        for i in range(1,256):
                                ip = (f"{_1}.{_2}.{_3}.{i}", 33333)
                                t(target=self.connect, args=(ip)).start()

        def connect(self, *ip):
                try:
                        print (ip)
                        o = socket.socket()
                        o.settimeout(3)
                        o.connect(ip)
                        o.send("WHO".encode())
                        print ("reached")
                        self.nick.append(Nick(o.recv(3333).decode()[:-1], ip[0]))
                except:
                        pass

class service(socket.socket):
        def __init__(self):
                super().__init__()
                self.bind(("0.0.0.0", 33333))
                self.nick = input("set nick> ")

        def command(self, client, msg):
                d = {"WHO": "client.send(self.nick.encode())"}
                if msg in d.keys():
                        eval(d[msg])

        def loop(self):
                pid = os.getpid()
                self.listen(0)
                while True:
                        client, addr = self.accept()
                        os.fork()
                        if os.getpid() == pid:
                                continue
                        else:
                                while True:
	                                asd = client.recv(1080)
	                                if not asd:
		                                break
	                                else:
		                                self.command(client, asd.decode())
                                client.close()



#o = service()
#o.loop()

o = discover()
print (o.nick)