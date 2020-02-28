import os
import time

def isConnected():
    current = time.time()
    #    print("PRINT " + str(os.system("/usr/bin/w3m -dump download.jovenclub.cu | grep h5ai")))
    #    CODE = os.system("/usr/bin/w3m -dump download.jovenclub.cu | grep h5ai &>/dev/null")
    CODE = os.system("/usr/bin/curl -s -m 10 --connect-timeout 5 download.jovenclub.cu | grep h5ai &>/dev/null")
    if CODE == 0:
        print (f"take {int (time.time() - current)}s long")
        return 0
    else:
        print (f"take {int (time.time() - current)}s long")
        return 1

def main():
    last_state=None
    counter=0
    while True:
        
        time.sleep (1)

        if  isConnected() == 0:   # CONNECT
            if last_state == True:
                print (f" {counter}:  already true in last state")
            counter = counter+1
            last_state=True
        else:               # not CONNECT
            if not last_state:
                print (f" {counter}:  already false bell")
            else:
                os.system("/usr/bin/timeout 3 mpv --no-video bell.ogg")
            last_state=False
            counter = counter+1            


if __name__ == "__main__":
    try :
        main()
    except:
        import sys
        sys.exit(0)
