with open("input.txt", "r")as file:
	num=file.readline()
	i=0
	star1=0
	star2=0
	while i<len(num):
		if num[i]==num[(i+1)%len(num)]:
			star1+=int(num[i])
		if num[i]==num[(i+len(num)/2)%len(num)]:
			star2+=int(num[i])
		i+=1
	print "star1:", star1
	print "star2:", star2

