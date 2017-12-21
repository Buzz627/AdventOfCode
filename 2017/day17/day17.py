mem=[0]
steps=382
num=1
pos=0
while num<=50000000:
	pos=(pos+steps)%num
	# print pos
	# mem.insert(pos,num)

	# print mem
	pos+=1
	if pos==1:
		print num
		print pos
		# print len(mem)
	# print num
	# print mem[0]
	# print pos
	# print ""
	num+=1
	
# print mem[0]
# print mem[mem.index(2017)+1]
