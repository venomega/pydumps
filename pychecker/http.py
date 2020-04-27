#!/usr/bin/env python3

import socket as s
#request="""GET / HTTP/1.1\r\nUser-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3\r\nHost: 200.55.184.81\r\nAccept-Language: en, mi\r\n\r\n"""
request="""GET / HTTP/1.1
User-Agent: */*
Host: 200.55.184.81

"""
HOST = "200.55.184.81"
PORT = 80
with s.socket(s.AF_INET,s.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.send(request.encode())
    incoming = sock.recv(1080)
    asd = incoming.decode()
    if "h5ai" in asd:
        exit(1)
    else:
        if "https://secure.etecsa.net:8443" in asd:
            exit(2)
        else:
            
            exit(0)
