results={(0, 0):1}
def getNeighborSum(pos):
	total=0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if i==0 and j==0:
				pass
			x, y=(pos[0]+i, pos[1]+j)
			if (x, y) in results:
				# print x, y
				total+=results[(x, y)]
	return total

directions=["+x", "+y", "-x", "-y"]
currentDir=0
lengthOfLeg=1
posInLeg=1


num=347991
# num=9

pos={"x":0, "y":0}


currentNum=2

while currentNum<=num:
	
	if posInLeg>lengthOfLeg:
		posInLeg=1
		if directions[currentDir][1]=="y":
			lengthOfLeg+=1
		currentDir=(currentDir+1)%4

	direct=directions[currentDir]
	if direct[0]=="+":
		move=1
	elif direct[0]=="-":
		move=-1

	pos[direct[1]]+=move
	results[(pos['x'], pos['y'])]=getNeighborSum((pos['x'], pos['y']))
	currentNum+=1
	posInLeg+=1
	# if results[(pos['x'], pos['y'])]>num:
	# 	print results[(pos['x'], pos['y'])]
	# 	break
	













	
	

print abs(pos['x'])+abs(pos['y'])
# print results
print pos




