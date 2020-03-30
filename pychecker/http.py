#!/usr/bin/env python3

import socket as s


HOST = "200.55.184.81"
PORT = 80
request=f"""GET / HTTP/1.1
User-Agent: */*
Host: {HOST}

"""

with s.socket(s.AF_INET,s.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.send(request.encode())
    asd = sock.recv(1080).decode()

    if "h5ai" in asd:
        exit(1)
    else:
        if "https://secure.etecsa.net:8443" in asd:
            exit(2)
        else:
            
            exit(0)
