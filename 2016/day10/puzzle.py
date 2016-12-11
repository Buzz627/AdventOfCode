with open("input.txt", 'rb')as inputfile:
	bots=[]
	for line in inputfile:
		line=line.split()
		if len(line)==6:
			bots.append(line[5])

	bots.sort()
	print bots