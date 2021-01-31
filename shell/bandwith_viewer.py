import os
import sys
import time


if not sys.platform == 'linux':
    sys.exit(print ("Sorry , you can`t use this script"))


iface = sys.argv[-1]
if 'py' in iface:
    sys.exit(print ("Usage:\n\tpython3 <program> ifname (ej: eth0)"))

old = [0,0]
path = "/sys/class/net"
tx = path + '/' + iface + '/' + 'statistics' + '/' + 'tx_bytes'
rx = path + '/' + iface + '/' + 'statistics' + '/' + 'rx_bytes'

while True:
    t, x = int(open(tx).read()), int(open(rx).read())
    print ("\b"*99, end='', flush=True)
    new= [t,x]
    print(f"TX: %.2f\tRX: %.2f\tBW: %.3f    " % (t/1000, x/1000, ((new[0]-old[0]+new[1]-old[1])/1000)), end="", flush=True)
    old=[t,x]
    time.sleep(1)
