import os
import json
import sys

d = dict()

try:
    d = json.load(open("bandwith.json"))
except:
    json.dump(d,open("bandwith.json","w"))
    d = json.load(open("bandwith.json"))
    
IF="ens192"
PATH="/sys/class/net/%s/statistics" %IF
TOTAL=0
BYTES=os.popen("cat %s/*bytes" %PATH).read().split()
MONTH, YEAR = os.popen("cal").read().split()[:2]

for i in BYTES:
    TOTAL+=int(i)
print (TOTAL)

while True:
    if YEAR in d.keys(): #if year in file
        if MONTH in d[YEAR].keys(): #if month in file
            print ("MB:",(TOTAL - d[YEAR][MONTH]) //1000000, file=open("/tmp/bandwith","w"))
            break
        else: #if not month in file, create it
            d[YEAR][MONTH] = TOTAL
            continue
    else: #if not year in file, create it
        d[YEAR] = dict()
        continue

json.dump(d,open("bandwith.json","w"))