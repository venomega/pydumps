#!/usr/bin/env python3
"""
import os
import smtplib
class CustomSMTP(object):
    def launch(self,msg):
        HOST="181.225.231.12"  # SMTP PLAIN
        USER="guilleps92@nauta.cu"
        PASS="DHthhnZN"
        PORT=25
        smtp = smtplib.SMTP(HOST,PORT)
        smtp.login(USER,PASS)
        #smtp.helo()
        smtp.sendmail(USER,USER,f"From:{USER}\nSubject: connection\nTo: BoredMan\n\n{msg}")
"""
import sys
import smtplib
import os
HOST="181.225.231.12"  # SMTP PLAIN
PORT=25
USER="guilleps92@nauta.cu"
PASS="DHthhnZN"
msg = sys.argv[1] 
uptime = os.popen("uptime","r").read()
pid = os.getpid()
msg = msg +"\n" + uptime +"\n" + str(pid)

smtp=smtplib.SMTP(HOST,PORT)
smtp.login(USER,PASS)
smtp.sendmail(USER,[USER,"guilleoph@nauta.cu"],f"From:{USER}\nSubject: connection\nTo: BoredMan\n\n{msg}")
