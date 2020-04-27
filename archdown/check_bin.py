#!/usr/bin/env python3
import sys


def error(string):
    print (string, file=sys.stderr)
    exit(1)
    
def isBin():
    """
    check for necesary binary files
    """
    error = 0
    #w3m
    try:
        fd = open("/bin/w3m", "rb")
        fd.close()

    except:
        error("we dont find all necesary binaries: w3m")
    #Aria2c
    try:
        fd = open("/bin/aria2c", "rb")
        fd.close()
        
    except:
        error("we dont find all necesary binaries: aria2")
    return 1

if isBin()==1:
    exit(0)

