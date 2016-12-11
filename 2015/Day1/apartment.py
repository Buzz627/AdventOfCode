with open('input.txt', 'rb') as inputFile:
	total=0
	pos=0
	for line in inputFile:
		for c in line:
			pos+=1
			if c=="(":
				total+=1
			elif c==")":
				total-=1
			if total<0:
				print pos
print total
