#!/usr/bin/env python3
import os
import sys
import time
os.chdir(f"{sys.path[0]}")
pwd = sys.path[0]
dbs = open(os.path.join(pwd,"dbs.conf"), "r").read().split()
arch= open(os.path.join(pwd,"arch.conf"), "r").read()[:-1]
for db in dbs:
    token =os.popen(f"ls ./mirror/{arch}/{db}/","r" ).read()
    fd = open("/tmp/asdasdasd","w")
    fd.write(token)
    fd.close()
    fd = open("/tmp/asdasdasd","r")
    f = open(f"./mirror/{arch}/{db}.list","r")
    asd = f.read()
    for i in fd:
        if "index" in i or "list" in i or "db" in i or "fetch" in i or ".aria2" in i:
            continue
        if i not in asd:
            print (i)
            os.system(f"/usr/bin/rm ./mirror/{arch}/{db}/{i}")
    
for db in dbs:
    command = f"ls -lh ./mirror/{arch}/{db}/ | grep .pkg.tar. | grep 343"
    token = os.popen(command).read()
    fd = open("/tmp/dump", "w")
    fd.write(token)
    fd.close()
    fd = open("/tmp/dump", "r")
    
    for i in fd:
        
        os.popen(f"rm ./mirror/{arch}/{db}/{i.split()[-1]}","r")
        
        
    
