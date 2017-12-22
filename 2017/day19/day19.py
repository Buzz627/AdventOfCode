
matrix=[]
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open ("input.txt", "r") as f:
	for line in f:
		matrix.append(list(line))
for row in matrix:		
	print row
y=0
x=matrix[y].index("|")
star1=""
direction=0
# moves["1":0, "2":0, "3":0, "0":1]
moves=0
while True:
	char=matrix[y][x]
	# print direction, y, x, char
	moves+=1
	if direction==0:
		if char in "|-":
			y+=1
		if char=="+":
			if (y+1)<len(matrix): 
				if matrix[y+1][x] not in [" ", "\n"]:
					y+=1
					continue
			if matrix[y][x+1] not in [" ", "\n"]:
				x+=1
				direction=3
				continue
			if matrix[y][x-1] not in [" ", "\n"]:
				x-=1
				direction=1
				continue
		if char in letters:
			star1+=char
			y+=1



	if direction==2:
		if char in "|-":
			y-=1
		if char=="+":
			if matrix[y-1][x] not in [" ", "\n"]:
				y-=1
				continue
			if matrix[y][x+1] not in [" ", "\n"]:
				x+=1
				direction=3
				continue
			if matrix[y][x-1] not in [" ", "\n"]:
				x-=1
				direction=1
				continue
		if char in letters:
			star1+=char
			y-=1

	if direction==1:
		if char in "|-":
			x-=1
		if char=="+":
			if matrix[y][x-1] not in [" ", "\n"]:
				x-=1
				continue
			if y+1<len(matrix):
				if matrix[y+1][x] not in [" ", "\n"]:
					y+=1
					direction=0
					continue
			if matrix[y-1][x] not in [" ", "\n"]:
				y-=1
				direction=2
				continue
		if char in letters:
			star1+=char
			x-=1

	if direction==3:
		if char in "|-":
			x+=1
		if char=="+":
			if matrix[y][x+1] not in [" ", "\n"]:
				x+=1
				continue
			if y+1<len(matrix):
				if matrix[y+1][x] not in [" ", "\n"]:
					y+=1
					direction=0
					continue
			if matrix[y-1][x] not in [" ", "\n"]:
				y-=1
				direction=2
				continue
		if char in letters:
			star1+=char
			x+=1
	if char in [" ", "\n"]:
		break
	


print star1
print moves-1



