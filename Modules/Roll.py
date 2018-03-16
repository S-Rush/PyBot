import random
import urllib.request
def handle(f,sender,msg,loc,rsvp,send):
	msg = msg.lower()
	parts = msg.split(' ',1)
	command = parts[0]
	if command==".roll":
		stri = "You rolled"
		args = parts[1].split('d',1)
		for n in range(0,min(int(args[0]),10)):
			roll = random.randint(1,min(int(args[1]),100))
			stri += " "+str(roll)
		rsvp(f,loc,stri)
def privhandle(f,sender,msg,loc,rsvp,send):
	handle(f,sender,msg,loc,rsvp,send)