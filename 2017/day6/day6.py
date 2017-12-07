def findMax(lst):
	m=0
	for i in range(len(lst)):
		if lst[i]>lst[m]:
			m=i

	return m



memory=[14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
# memory=[0,2,7,0]
intertions=[]
temp=" ".join(map(str, memory))
star1=0
while temp not in intertions:
	intertions.append(temp)
	star1+=1
	index=findMax(memory)
	num=memory[index]
	memory[index]=0
	for i in range(1, num+1):
		memory[(index+i)%len(memory)]+=1
	temp=" ".join(map(str, memory))
	# print memory



print star1
print star1-intertions.index(temp)
