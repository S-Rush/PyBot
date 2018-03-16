def handle(f,sender,msg,loc,rsvp,send):
	parts = msg.split(' ',2)
	command = parts[0]
	if command==".help":
		if len(parts)==1 or parts[1]=='':
			rsvp(f,loc,"Modules include 8ball, inspire, roa, and roll. Use '.help <modulename>' for more information.")
		elif parts[1]=="8ball":
			rsvp(f,loc,"To roll the eight ball, simply use '.8ball <Question>'.")
		elif parts[1]=="inspire":
			rsvp(f,loc,"To be inspired, simply say 'inspire' or 'inspiration' in a message. In fact, you did it just now!")
		elif parts[1]=="roa":
			rsvp(f,loc,"To see a rule of acquisition, simply say '.roa' or use 'rule(s) of acquistion' or 'ferengi' in a message.")
		elif parts[1]=="roll":
			rsvp(f,loc,"To roll dice, simply use '.roll <n>d<m>' to roll n dice with m sides.")
def privhandle(f,sender,msg,loc,rsvp,send):
	handle(f,sender,msg,loc,rsvp,send)