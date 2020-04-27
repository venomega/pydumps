#!/usr/bin/env python3
import os
import sys
os.chdir(sys.path[0])

dbs=open("dbs.conf", "r").read().split()
arch=open("arch.conf", "r").read()[:-1]
total= 0
fore= open(f"./mirror/{arch}/size", "w")
for db in dbs:
    
    os.system(f"/usr/bin/w3m -dump download.jovenclub.cu/repos/archlinux/{db}/os/{arch}/ > /tmp/dump")

    fd = open("/tmp/dump","r")
    file = open(f"./mirror/{arch}/{db}.list","w")
    counter= 0.0

    for i in fd:
        if not "pkg.tar." in i:
            continue
    
        token = i.split()
        print (token[1], file=file)
        if token[-1] == "KB":
            counter += int(token[-2])
        else:
            counter += int(token[-1])

    print (f"{db.upper()}\t\t %.2f MB " % (counter / 1000), file=fore)
    total += counter / 1000
    fd.close()

print (f"TOTAL\t\t %.2f MB" %(total), file=fore)

