import socket as ss
import os
import sys


try:
	HOST = (sys.argv[1],int(sys.argv[2]))
except:
	print ("usage:\n\n\tprogram <host> <port>")
	exit(1)

def session(c):
	prompt = c.recv(1080)
	while True:
		req = input(prompt.decode())
		c.send(req.encode())
		resp = c.recv(33000)
		print (resp.decode(),end="",flush=True)

def main():
	o = ss.socket()
	try:
		o.connect(HOST)
		session(o)
	except KeyboardInterrupt:
		pass
	except:
		print ("Connection error",file=sys.stderr)
	o.close()
	exit(0)

if __name__ == "__main__":
	main()
