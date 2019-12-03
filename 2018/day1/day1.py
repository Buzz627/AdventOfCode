with open("input.txt", "r") as f:
	star1=0
	changes=[]
	for line in f:
		changes.append(line)
		star1+=int(line)
print "star1 {}".format(star1)

i=0
star1=0
while i<len(changes):
	star1+=int(changes[i%len(changes)])
	i+=1
print "star1 {}".format(star1)

i=0
seen=[]
star2=0
# changes=[+7, +7, -2, -7, -4]
while star2 not in seen:
	seen.append(star2)
	# print seen
	star2+=int(changes[i%len(changes)])
	i+=1


print "star2 {}".format(star2)


