verifies = {}
def handlestatus(f,msg,rsvp):
	parts = msg.split(' ')
	if parts[0]=="STATUS": # We are dealing with a status message
		if parts[2]=="3": # Status is identified
			verifies[parts[1]]() # Run the callback
			verifies[parts[1]] = [] # Then delete it
		else: # Status is not identified
			verifies[parts[1]] = [] # Delete the callback in verifies for this user

def handle(f,sender,msg,loc,rsvp,send,admodules,auths):
	rsvp(f,"NickServ","STATUS "+sender) # Ask NickServ to check their status
	def run_admods():
		for admodule in admodules:
			try:
				if sender == loc:
					admodule.privhandle(f,sender,msg,loc,rsvp,send,auths)
				else:
					admodule.handle(f, sender, msg, loc, rsvp, send, auths)
			except (ValueError, IndexError, AttributeError) as e:
				print(e)
				return
	verifies[sender] = run_admods