def comhandle(line,f,rsvp,send):
	line = line.strip("\n")
	parts = line.split(' ',1)
	if parts[0].lower()=='send':
		send(f,parts[1])