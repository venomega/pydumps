#!/usr/bin/python3
import json
import sys
import os


ip = sys.argv[1]

d = json.loads(os.popen(f"w3m -dump http://ip-api.com/json/{ip}").read())

print (d['query'],"\n",d['country'],"\n", d['isp'],"\n",d['org'])
