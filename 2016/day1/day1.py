with open('input.txt', 'rb') as inputFile:
	directions=["north", "east", "south", "west"]
	distance={"north":0,"east":0, "south":0, "west":0}
	facing=0
	for line in inputFile:
		distance={"north":0,"east":0, "south":0, "west":0}
		facing=0
		line=line.split(", ")
		x=0
		y=0
		places=[]
		for i in line:
			# print i[1:]
			if i[0]=="R":
				facing+=1
			elif i[0]=="L":
				facing-=1
			else:
				print "eggeg"
			facing%=4
			# print directions[facing]
			tempx=x
			tempy=y
			for j in range (int(i[1:])):
				if facing==0:
					tempy+=1
				elif facing ==2:
					tempy-=1
				elif facing == 1:
					tempx+=1
				elif facing ==3:
					tempx-=1
				if (tempx, tempy) in places:
					print tempx,tempy, abs(tempx)+abs(tempy)
				places.append((tempx, tempy))
			if facing==0:
				y+=int(i[1:])
			elif facing ==2:
				y-=int(i[1:])
			elif facing == 1:
				x+=int(i[1:])
			elif facing ==3:
				x-=int(i[1:])
			else:
				print "somethng wrong"

			

		print abs(x)+abs(y)
		print x, y
		print "\n\n"
		# print distance
		# print abs(distance["north"]-distance["south"])+abs(distance["east"]-distance["west"])
