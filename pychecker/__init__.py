#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import socket as s

def isConnected():
    pwd = sys.path[0]
    try:
        r = subprocess.run(os.path.join(pwd,"http.py"),timeout=12)
        code = r.returncode
        if code == 1:
            return 0
        else:
            return 1
    except:
        return 1

def mail(string):
    pwd = sys.path[0]
    try:
        r = subprocess.run([os.path.join(pwd,"mail.py"),f"{string}"],timeout=7)
    except:
        print ("OOPS :)")

def main():

    last_state=None
    counter=0
    
    while True:
        
        time.sleep (1)
        print ("asd")
        token = isConnected()
        if  token == 0:   # CONNECT
            print ("pass")
            if last_state == True:
                print (f" {counter}:  already true in last state")
                asd = None
            else:
                fd = os.popen("date", "r")
                mail(f"connected at {fd.read()}")
            counter = counter+1
            last_state=True
        else:               # not CONNECT
            print ("no pass")
            if not last_state:
                asd = None
                print (f" {counter}:  already false bell")
            else:
                sound_the_alarm= None
                os.system("/usr/bin/timeout 3 mpv --no-video bell.ogg")
            last_state=False
            counter = counter+1            


if __name__ == "__main__":
    """
    try :
        main()
    except:
        import sys
        sys.exit(0)
    """
    main()
