#!/usr/bin/env python3
import sys
import os

os.chdir(sys.path[0])

dbs = open("dbs.conf","r").read().split()
arch= open("arch.conf","r").read()[:-1]

for i in range(len(dbs)):
    os.popen(f"mkdir -p ./mirror/{arch}/{dbs[i]}")
