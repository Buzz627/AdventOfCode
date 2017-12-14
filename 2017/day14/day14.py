from day10 import knotHash

def toBin(num):
	output=""
	for k in num:
		output+="{:0>4}".format(bin(int(k, 16))[2:])
	return output

def getGroups(data):
	marker=2
	stack=[]
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j]=='1':
				stack.append((i, j))
				while len(stack)>0:
					current=stack.pop()
					x=current[0]
					y=current[1]
					data[x][y]=str(marker)
					
					if data[min(x+1, len(data)-1)][y]=="1":
						stack.append((min(x+1, len(data)-1), y))
				
					if data[max(x-1, 0)][y]=="1":
						stack.append((max(x-1, 0), y))
				
					if data[x][min(y+1, len(data[x])-1)]=="1":
						stack.append((x, min(y+1, len(data[x])-1)))
					
				
					if data[x][max(y-1, 0)]=="1":
						stack.append((x, max(y-1, 0)))
					
					# print stack
				marker+=1

				# for d in data[:8] :print d[:8]
				# print ""
	print marker-2




key="ugkiagan"
# key="flqrgnkx"
# key="a0c2017"

count=0
full=[]
for i in range(128):
	# print key+"-"+str(i)
	temp=knotHash(key+"-"+str(i))
	# print temp	
	b=toBin(temp)
	# print b
	full.append(list(b))
	for j in b:
		if j=='1':
			count+=1
print count
# print full
getGroups(full)




