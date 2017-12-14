with open("input.txt", "r") as f:
	stream=f.readline()
	# stream='''{{{},{},{{}}}}'''
	count=0
	star1=0
	star2=0
	i=0
	while i<len(stream):
		if stream[i]=="{":
			count+=1
			star1+=count
		elif stream[i]=="!":
			i+=1
		elif stream[i]=="}":
			count-=1
		if stream[i]=="<":
			i+=1
			while stream[i]!=">":
				if stream[i]=="!":
					i+=1
				else:
					star2+=1
				i+=1
		# print count


		i+=1
print count
print star1
print star2
