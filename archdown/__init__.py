import sys
import os
import subprocess as s

def mandatory():
    os.chdir (sys.path[0])
    print ("Preparing directory")
    r=s.run("./preparedir.py")

    if not "-n" in sys.argv:
        print ("Downloading list")
        r=s.run("./getlist.py")
    if not "-f" in sys.argv:
        print ("Removing garbage")
        r=s.run("./flush.py")
    
    print ("Checking binaries")
    r=s.run("./check_bin.py")
    if r.returncode != 0:
        exit(1)

def launch():
    print ("Download started")
    r=s.run("./down_them_all.py")

## MAIN CODE
if len(sys.argv) == 1:
    print (" -n not download database list\n -f not flush files\n -q not download files\n\n -d run in daemon mode\n -l run in foreground mode")
    exit (0)
mandatory()

if "-d" in sys.argv:
    pid = os.getpid()
    os.fork()
    if os.getpid() == pid:
        exit(0)
    else:
        os.popen(f"echo '{os.getpid()}' > PID")
        # CICLE
        launch()
else:
    if not "-q" in sys.argv:
        launch()


    
