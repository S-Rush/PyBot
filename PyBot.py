# A simple IRC Bot written in Python3
# Copyright Sam Rush 2017
# Use this however you want I guess
# Sorry for not having an actual license on this—I didn't intend for it to be something I shown as anything more than an example to a high school coding club

# Imports
import socket
import time
import random
import sys
import select
import glob
import importlib

import AdminHandler as Admin

# Bring in the modules
modules = []
for module_name in glob.glob("Modules/*.py"):
	if module_name[8:-3] != "__init__":
		modules.append(importlib.import_module('Modules.'+module_name[8:-3]))
# Bring in the authorization modules
admodules = []
for module_name in glob.glob("AdModules/*.py"):
	if module_name[10:-3] != "__init__":
		admodules.append(importlib.import_module('AdModules.'+module_name[10:-3]))
# Bring in the command line modules
commodules = []
for module_name in glob.glob("ComModules/*.py"):
	if module_name[11:-3] != "__init__":
		commodules.append(importlib.import_module('ComModules.'+module_name[11:-3]))

# Start with some configuration
network = "irc.rizon.net"
port = 6663
nick = "PyBot"
username = "PyBot"
realname = "PyBot"
channels = {"#testchannel"}
auths = {"AdminExample": [1,2], "ModExample": [2]}
# Auths Level List:
# 1 : Administrator
# 2 : Moderator

s = socket.socket()
nonblock = 0

# Method to start everything up
def runBot():
	global nonblock
	s.connect((network, port))
	print('Socket connected to '+network+':'+str(port))
	f = s.makefile('rw')
	send(f, "NICK "+nick)
	send(f, "USER "+username+" "+"ignore"+" "+"ignore"+" "+" :"+realname)
	while True:
		if nonblock:
			curin = select.select([s,sys.stdin],[s],[])
			if s in curin[0]:
				onreceive(f,f.readline())
			elif sys.stdin in curin[0]:
				oninput(f,sys.stdin.readline())
		else:
			onreceive(f,f.readline())
		
# Functions to handle basic things
	
def sendform(line):
	return bytes(line+"\r\n", 'UTF-8')

def send(f, line):
	f.write(line+"\r\n")
	f.flush()
	print(line)

def onreceive(f,line):
	line = line.strip("\n")
	print(line)
	if line=='':
		return
	commanddispatch(f,line)

def oninput(f,line):
	global commodules
	for commodule in commodules:
		try:
			commodule.comhandle(line,f,rsvp,send)
		except (ValueError, IndexError, AttributeError, TypeError) as e:
			print(e)
			return

def commanddispatch(f,line):
	global nonblock
	parts = ['', '', '']
	if line[0]==':': # Has a sender
		parts = line.split(' ', 2)
		# Note the parts will now be as follows:
		# 0 : Sender
		# 1 : Command
		# 2 : Remainder
	else: # No sender
		firstparts = line.split(' ', 1)
		for i in range(0,2):
			parts[i+1] = firstparts[i]
		# Sorry this is a terrible way to do it but I forgot at first that not everything has a sender
	command = parts[1]
	if command=="PING":
		pong(f,parts)
	elif command=="376":
		for channel in channels:
			send(f, "JOIN "+channel)
		send(f, "PRIVMSG NickServ :IDENTIFY Canbobfly786!")
		send(f, "PRIVMSG HostServ :ON")
		s.setblocking(0)
		nonblock = 1
	elif command=="PRIVMSG" or command=="NOTICE":
		msgprehandler(f, parts)

def rsvp(f, loc, msg):
	send(f, "PRIVMSG "+loc+" :"+msg)
		
# Functions for each command are here now
def pong(f, parts):
	send(f,"PONG "+parts[2])

def msgprehandler(f, parts):
	msgparts = parts[2].split(' :',1)
	sender = parts[0].split('!')[0].strip(':')
	destination = msgparts[0]
	msg = msgparts[1].strip('\n')
	if destination[0]=="#": # channel message
		chanmsghandler(f, sender, msg, destination)
	else: # private message
		usrmsghandler(f, sender, msg)

def chanmsghandler(f, sender, msg, chan):
	global modules
	parts = msg.split(' ',1)
	command = parts[0]
	try:
		if command==".admin":
			Admin.handle(f,sender,msg,chan,rsvp,send,admodules,auths)
	except (ValueError, IndexError, AttributeError, TypeError, KeyError) as e:
		print(e)
		return
	for module in modules:
		try:
			module.handle(f,sender,msg,chan,rsvp,send)
		except (ValueError, IndexError, AttributeError, TypeError) as e:
			print(e)
			return	
def usrmsghandler(f, sender, msg):
	global modules
	global admodules
	parts = msg.split(' ',1)
	command = parts[0]
	if command==".join":
		if sender in adminnicks:
			send(f, "JOIN "+parts[1])
	try:
		if sender=="NickServ":
			Admin.handlestatus(f,msg,rsvp)
		if command==".admin":
			Admin.handle(f,sender,msg,sender,rsvp,send,admodules,auths)
	except (ValueError, IndexError, AttributeError, TypeError, KeyError) as e:
		print(e)
		return
	for module in modules:
		try:
			module.privhandle(f,sender,msg,sender,rsvp,send)
		except (ValueError, IndexError, AttributeError, TypeError) as e:
			print(e)
			return

# Now we can just call runBot() and let everything happen
runBot()
print('Bot ended execution.')
