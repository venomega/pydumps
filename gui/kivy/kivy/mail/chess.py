
import curses
import time
import os
import sys
import email

USER="guilleps92@nauta.cu"
PASS="DHthhnZN"
DEST=USER
IMAP_HOST = "181.225.231.14"
IMAP_PORT = 143
SSL = False
dict ={'USER':USER,'PASS':PASS,'DEST':DEST,
	'IMAP_HOST':IMAP_HOST,'IMAP_PORT':IMAP_PORT,"SSL":SSL,}


def send(d):
	import smtplib
	print (d)
	USER= d["USER"]
	PASS= d['PASS']
	DEST= d['DEST']
	object = smtplib.SMTP("181.225.231.12",25)
	check= object.login(USER,PASS)
	if check[1] != b'2.7.0 Authentication successful' :
		print("Error authenticating")
		exit(1)
	del check
	check = object.sendmail(USER, [DEST], f"FROM: {USER}\nTO: {DEST}\nSUBJECT: Chess\n\nsuccess")
	print ("Success") if check == {} else print ("Destinatary unreachable")
def set_mail_seen(object, byte):
	object.uid("store", byte, "FLAGS", "\\SEEN")
def _set_mail_unseen(object, byte):
	object.uid("store", byte, "-FLAGS", "\\SEEN")

def _get_body_lines(path):
	fd = open(path, "r")
	count = 0
	for i in fd:
		count +=1
	response = _get_line(path, count-1)
	print ("asd", response)
	fd.close()
	return response
def _get_line(path, count):
	fd = open(path, "r")
	token = 0
#	print (count)
	for i in fd:
		if count == token:
			return i
			break
		token +=1
#	print (token)
def _get_body(msg):
	fd = open("raw.txt", "w")               # this has to change in every platform
	print (msg, file=fd, end="")
	fd.close()
	return str(  _get_body_lines("raw.txt"))
	
def _check_mail(object, byte):
	code, response = object.uid("fetch", byte, '(RFC822)') # fetching email
	raw = response[0][1]                           #/**********************************
	string = raw.decode('utf-8')                   #
	email_msg = email.message_from_string(string)  # Analizing incoming email
	#print (email_msg['From'])                      #
	if email_msg['Subject'] != "Chess":  #cancel wrong chess email
		_set_mail_unseen(object,byte)
		return
	body = _get_body(email_msg)               # /************************************
	print (body)		  # get body/chess_command

def recv(dict):
	import imaplib
	USER = dict['USER']
	PASS = dict['PASS']
	HOST = dict['IMAP_HOST']
	PORT = dict['IMAP_PORT']
	object = imaplib.IMAP4(HOST, PORT)
	object.login(USER,PASS)
	object.select()
	code, response = object.uid("search", None, 'UNSEEN')
	if code != "OK" :
		print ("error getting code", code)
		exit(1)
	unseen = response[0].split()
	print (unseen)
	for mail_byte_id in unseen:
		_check_mail(object, mail_byte_id)
		#break

send(dict)
#time.sleep(1)
#recv(dict)

