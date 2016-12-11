def possible(arr):
	for i in arr:
		if i>=sum(arr)-i:
			return False
	return True

def readNums(s):
	s=s.strip().split()
	nums=[]
	for i in s:
		if i.isdigit():
			nums.append(int(i))
	return nums
	
def readTrips(a):
	s="".join(a)
	nums=readNums(s)
	a=[]
	b=[]
	c=[]
	for i in range(3):
		a.append(int(nums[i*3]))
		b.append(int(nums[(i*3)+1]))
		c.append(int(nums[(i*3)+2]))
	return [a,b,c]


with open("input.txt", "rb") as inputfile:
	total=0
	triple=[]
	for line in inputfile:
	# for j in range(6):
		# line=inputfile.next()
		triple.append(line)
		if len(triple)<3:
			continue

		# print triple
		for i in readTrips(triple):
			# print i
			if possible(i):
				total+=1
		triple=[]
	print total