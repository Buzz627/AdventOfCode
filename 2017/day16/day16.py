
def rotate(lst, num):
	return lst[-num:]+lst[:-num]

	

def swapIndex(lst, a, b):
	temp=lst[a]
	lst[a]=lst[b]
	lst[b]=temp
def swapPro(lst, a, b):
	a=lst.index(a)
	b=lst.index(b)
	swapIndex(lst, a, b)


test="s1,x3/4,pe/b"

iterations=[]
programs=list("abcdefghijklmnop")
# programs=rotate(programs, 1)
with open ("input.txt", "r")as f:
	for line in f:
		current="".join(programs)
		# while current not in iterations:
		# 	iterations.append(current)
		for times in xrange(1000000000%60):
			lst=line.split(",")
			for i in lst:
				nums=i[1:].split("/")
				# print i[0],nums
				
				if i[0]=="s":
					programs=rotate(programs, int(nums[0]))
				if i[0]=="x":
					swapIndex(programs, int(nums[0]), int(nums[1]))
				if i[0]=="p":
					swapPro(programs, nums[0], nums[1])
			current="".join(programs)
print "".join(programs)
print len(iterations)
