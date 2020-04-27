#!/usr/bin/env python3
import sys
import smtplib
import os
HOST="181.225.231.12"  # SMTP PLAIN
PORT=25
USER=""
PASS=""
msg = sys.argv[1] 
uptime = os.popen("uptime","r").read()
pid = os.getpid()
msg = msg +"\n" + uptime +"\n" + str(pid)

smtp=smtplib.SMTP(HOST,PORT)
smtp.login(USER,PASS)
smtp.sendmail(USER,[USER,"guilleoph@nauta.cu", "near1297@nauta.cu"],f"From:{USER}\nSubject: connection\nTo: BoredMan\n\n{msg}")
