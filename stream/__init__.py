
#!/usr/bin/env python3
import socket
import sys

def help():
        print ("USAGE:\n <syntax>\n program <option> <ip address> </file/to/send>\n\n<options>\n send\nrecv", file=sys.stderr)
        exit(1)

class stream(object):
        """
        This library is a simple way to send and receive files in a specific port(33333)
        
        EXAMPLE 1:
        
        peer 1   <=   ip: 1.1.1.1
        >>> import socket
        >>> s = socket.socket()
        >>> s.serv_send("./file/to/send")
        
        peer 2  <= ip 1.1.1.2
        >>> import socket
        >>> s = socket.socket()
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

        

