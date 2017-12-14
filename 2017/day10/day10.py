lst=range(256)
lengths=[3, 4, 1, 5, 17, 31, 73, 47, 23]

lengths=46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204
inputstr='46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'
# inputstr=''


def knotHash(seed):
	lengths=map(lambda x:ord(x), inputstr)+[17, 31, 73, 47, 23]
	skip=0
	pos=0

	for times in range(64):
		for get in lengths:
			temp=[]
			for i in range(get):
				temp.append(lst[(pos+i)%len(lst)])
			temp=temp[::-1]
			# print temp
			for i in range(len(temp)):
				lst[(pos+i)%len(lst)]=temp[i]
			# print lst
			pos+=(len(temp)%len(lst))+skip
			skip+=1

	# print lst
	dense=[]
	star2=""
	for i in range(16):
		num=reduce(lambda x, y:x^y, lst[i*16:(i*16)+16])
		dense.append(num)
		star2+='{:0>2}'.format(hex(num)[2:])
	# print star2
	# print dense
	return star2


print knotHash(inputstr)


