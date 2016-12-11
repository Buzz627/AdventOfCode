import md5
password=[None]*8
found=0
start="reyedfim"
count=0
while found<8:
	char=md5.new(start+str(count)).hexdigest()
	if char[0:5]=="00000" and int(char[5], 16)<8:
		if password[int(char[5])] == None:
			password[int(char[5])]=char[6]
			found+=1
	count+=1
print "".join(password)
