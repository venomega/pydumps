#!/usr/bin/env python3
import sys
import os
os.chdir (sys.path[0])
PID = open("PID", "r").read().split()

for i in range(len(PID)):
    os.popen(f"kill {PID[i]}")

os.popen("killall aria2c")
