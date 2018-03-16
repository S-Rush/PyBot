def handle(f,sender,msg,loc,rsvp,send,auths):
	if 1 not in auths[sender]:
		return
	parts = msg.split(' ')
	if parts[1]=="join":
		send(f,"JOIN "+parts[2])
	elif parts[1]=="amiadmin":
		rsvp(f,loc,"Yes")
	elif parts[1]=="kick":
		chan = parts[2]
		user = parts[3]
		send(f,"KICK "+chan+" "+user)
	elif parts[1]=="part":
		send(f, "PART "+parts[2])
	elif parts[1]=="auths":
		try:
			rsvp(f,loc,parts[2]+" has auths "+str(auths[parts[2]])+".")
		except KeyError as e:
			try:
				rsvp(f,loc,parts[2]+" has no auths.")
			except KeyError as e2:
				print(e+"\n"+e2)
	elif parts[1]=="help":
		if len(parts)==2 or parts[2]=='':
			rsvp(f,loc,"Use admin commands with form '.admin <command> <arguments>'. Available command include join, part, amiadmin, kick, auths and help. For information on specific commands, use '.admin help <command>'. These commands are only usable by PM.")
		elif parts[2]=="help":
			rsvp(f,loc,"For information on a command, use '.admin help <command>'.")
		elif parts[2]=="join":
			rsvp(f,loc,"To have the bot join a channel, use '.admin join <channel>'.")
		elif parts[2]=="amiadmin":
			rsvp(f,loc,"To check if you are an admin, use '.admin amidamin'.")
		elif parts[2]=="part":
			rsvp(f,loc,"To have the bot part a channel, use '.admin part <channel>'.")
		elif parts[2]=="kick":
			rsvp(f,loc,"To have the bot kick a user from a channel, use '.admin kick <channel> <user>'.")
		elif parts[2]=="auths":
			rsvp(f,loc,"To see the list of auth tiers for a user, use '.admin auths <user>'.")
def privhandle(f,sender,msg,loc,rsvp,send,authtiers):
	handle(f,sender,msg,loc,rsvp,send,auths)