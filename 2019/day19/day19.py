import sys
sys.path.append("..")
from intCode import Calculator

def beamWidth(row):
	return len(list(filter(lambda x: x=="#", row)))

def printGrid(grid):
	for i in grid:
		print("".join(i))

def canFit(num, row, start):
	r=row[start:]
	return len(list(filter(lambda x: x=="#", r)))>=num

def getValue(c, x, y):
	c.restart()
	c.addInput(x)
	c.addInput(y)
	
	while not c.isFinished():
		result=c.calculate()
	return result

def findStartOfBeam(c, startx, y):
	x=startx
	while getValue(c, x, y)==0:
		# print(x, y)
		x+=1
	return x




inputArr=[109,424,203,1,21102,1,11,0,1105,1,282,21101,18,0,0,1106,0,259,2101,0,1,221,203,1,21102,1,31,0,1106,0,282,21101,0,38,0,1106,0,259,21002,23,1,2,22102,1,1,3,21101,0,1,1,21102,57,1,0,1106,0,303,2102,1,1,222,21002,221,1,3,21002,221,1,2,21101,0,259,1,21101,0,80,0,1105,1,225,21101,123,0,2,21101,91,0,0,1105,1,303,1201,1,0,223,20101,0,222,4,21101,259,0,3,21102,225,1,2,21101,0,225,1,21102,118,1,0,1105,1,225,21001,222,0,3,21102,58,1,2,21101,133,0,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1106,0,259,1201,1,0,223,20101,0,221,4,21002,222,1,3,21101,20,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,109,20207,1,223,2,20102,1,23,1,21101,-1,0,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22102,1,-3,1,22102,1,-2,2,22101,0,-1,3,21101,250,0,0,1105,1,225,21202,1,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21201,-2,0,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,1,343,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,1,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0]
c=Calculator(inputArr)

total=0


grid=[]


for y in range(50):
	row=[]
	for x in range(50):
		# print(x,y)
		result=getValue(c, x, y)

		if result==1:
			total+=1
			row.append("#")
		else:
			row.append(".")
		
	grid.append(row)
printGrid(grid)


print(total)



y=6
x=0

size=100

points=[getValue(c, x, y), getValue(c, x+(size-1), y), getValue(c, x, y+(size-1)), getValue(c, x+(size-1), y+(size-1))]
while 0 in points:
# for _ in range(20):
	# print(points)
	y+=1
	x=findStartOfBeam(c, x, y)
	# print(x, y)
	points=[getValue(c, x, y), getValue(c, x+(size-1), y), getValue(c, x, y-(size-1)), getValue(c, x+(size-1), y-(size-1))]


print(x, (y-(size-1)))

print((x*10000)+(y-(size-1)))
