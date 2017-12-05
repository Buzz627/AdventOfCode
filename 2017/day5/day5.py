jumps=[]
i=0
star1=0
with open("input.txt", "r")as f:
	for line in f:
		jumps.append(int(line))

while i<len(jumps):
	current=jumps[i]
	if jumps[i]>=3:
		jumps[i]-=1
	else:
		jumps[i]+=1
	i+=current
	star1+=1
print star1

