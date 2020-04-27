#!/usr/bin/env python3
import time

def isCopyTime():
    the_clock = (time.localtime())
    """
    # from `the_clock`
    # [3] =  h
    # [4] =  m
    # [5] =  s
    # [-3]=  week day # start from monday in 0, sunday is 6
    """
    print (the_clock)
    if the_clock[-3] > 4:
        print ("saturday-sunday")
        ## saturday and sunday
        if the_clock[3] > 3 and  the_clock[3] < 10:
            return 0
        else:
            return 1
    else:
        print ("monday-freeday")
        ## from monday to friday
        if the_clock[3] > 2 and  the_clock[3] < 12:
            return 0
        else:
            return 1

print (isCopyTime())
