def countCells(mat):
	count=0
	for row in mat:
		for cell in row:
			if cell=="#":
				count+=1
	return count

def makeRect(mat, row, col):
	for i in range(row):
		for j in range(col):
			mat[j][i]="#"

def rotateCol(mat, col, num):
	if num==0:
		return
	temp=mat[len(mat)-1][col]
	for i in range(len(mat)-1, 0, -1):
		mat[i][col]=mat[i-1][col]
	mat[0][col]=temp
	rotateCol(mat, col, num-1)

def rotateRow(mat, row, num):
	if num==0:
		return
	temp=mat[row][len(mat[row])-1]
	for i in range(len(mat[row])-1, 0, -1):
		mat[row][i]=mat[row][i-1]
	mat[row][0]=temp
	rotateRow(mat, row, num-1)

with open("input.txt","rb") as inputfile:
	pad=[["."]*50 for i in range(6)]
	# makeRect(pad, 3, 2)
	# for i in pad:
	# 	print i
	# rotateRow(pad, 1, 2)
	# print ""
	# for i in pad:
	# 	print i
	# print ""
	# rotateCol(pad, 2, 5)
	# for i in pad:
	# 	print i
	for line in inputfile:
		comm=line.strip().split()
		if len(comm)==2:
			# print comm[1]
			n=comm[1].split("x")
			# print n
			makeRect(pad, int(n[0]), int(n[1]))
		else:
			if comm[1]=="row":
				row=int(comm[2][2:])
				num=int(comm[4])
				# print row, num
				rotateRow(pad, row, num)
			if comm[1]=="column":
				col=int(comm[2][2:])
				num=int(comm[4])
				# print col, num
				rotateCol(pad, col, num)
	for i in pad:
		print " ".join(i)
	print countCells(pad)
	#efeykfrfij