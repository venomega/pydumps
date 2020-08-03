import os
import sys
import time


def doe(i):
	print (i)
	pid = os.getpid()
	os.fork()
	if os.getpid() != pid:
		code =os.popen(f"timeout 1 drill @{i} 2&>/dev/null; echo $?").read().split()
		print ("CODE",code)
		#code = int(code)
		if code[0] == '0':
			open("dns.raw","a").write(f"{i}\n")
		exit(0)

def show_me(): 
	li = open("dns.raw", "r").read().split()
	for i in li:
		print (os.popen(f"drill @{i} google.com | grep AAAA -A5 | grep SERVER").read())

def prepare(l1,l2,l3,l4):
	for _1 in l1:
		for _2 in l2:
			for _3 in l3:
				for _4 in l4:
					ip = f"{_1}.{_2}.{_3}.{_4}"
					#print (ip,end=" ")
					doe(ip)



def proccess(get):
	token = get.split(".")	
	end = []
	for r in token:
		if r != 'x':
			end.append([int(r)])
		else:   
			end.append(list(range(255)))
	return end

def main():
	#// get ip
	#get = "200.55.128.x"
	get = proccess(sys.argv[1])
	print (get)
	#// prepare for launch & launch
	prepare(get[0],get[1],get[2],get[3])





main()
