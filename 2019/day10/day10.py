import math

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

def countSight(coords, pos, par):
	# count=0
	# print(pos)
	# for p in par:

	# 	rise=p[1]-pos[1]
	# 	run=p[0]-pos[0]
	# 	num=abs(gcd(rise, run))
	# 	if num==0:
	# 		continue
	# 	rise=rise//num
	# 	run=run//num
	# 	temp=(pos[0]+run, pos[1]+rise)
	# 	while temp!=p:
	# 		if temp in coords:
	# 			print (" inside", temp)
	# 			count+=1
	# 			fount=True
	# 			break
	# 		temp=(temp[0]+run, temp[1]+rise)
	# 	if temp==p and temp in coords:
	# 		print("outside", temp)
	# 		count+=1
		
	# return count







	count=[]
	for c in coords:

		if c == pos:
			continue
		rise=c[1]-pos[1]
		run=c[0]-pos[0]
		num=abs(gcd(rise, run))

		rise=rise//num
		run=run//num
		temp=(pos[0]+run, pos[1]+rise)
		while temp!=c:
			if temp in coords:
				break
			temp=(temp[0]+run, temp[1]+rise)
		if temp==c:
			count.append(temp)

	return count

def getParimiter(x, y):

	parimeter=[]
	for i in range(y-1):
		parimeter.append((0, i))
	for i in range(x-1):
		parimeter.append((i, y-1))
	for i in range(y-1, 0, -1):
		parimeter.append((x-1, i))
	for i in range(x-1, 0, -1):
		parimeter.append((i, 0))
	return parimeter

def dotProduct(a, b):
	total=0
	for i in range(len(a)):
		total+=a[i]*b[i]
	return total

def vectorLength(vector):
	total=0
	for i in vector:
		total+=i**2
	return math.sqrt(total)



def getAngle(start, end):
	if start==end:
		return 0
	vector=(end[0]-start[0], end[1]-start[1])
	vector2=(0, -1)
	# print(vector2)
	# if vector[1]==0:
	# 	return 90
	# return math.degrees(math.atan(vector[0]/vector[1]))
	# angle=math.degrees(math.atan2(vector[0], vector[1]))+90
	dot=dotProduct(vector, vector2)
	len1=(vectorLength(vector))
	len2=(vectorLength(vector2))
	# print(end, vector, vector2)
	angle=math.degrees(math.acos(dot/(len1*len2)))
	if end[0]<start[0]:
		angle=360-angle



	return angle

def destroy(coords, pos):
	pass


	


def getDirection(coords, pos):
	# print(coords)
	angles=[]
	for c in coords:
		if c==pos:
			continue
		angles.append((c, getAngle(pos, c)))
	return sorted(angles, key=lambda x: x[1])
	
	

def getAstroidPos(space):
	result=[]
	for y in range(len(space)):
		for x in range(len(space[y])):
			if space[y][x]=="#":
				result.append((x,y))
	return result

with open("input.txt", "r")as f:
	space=[]
	for row in f:
		space.append(list(row.strip()))
	coords=getAstroidPos(space)
	# print(coords)
	# print(countSight(coords, coords[1]))
	par=getParimiter(len(space[0]), len(space))
	best=(countSight(coords, coords[0], par), coords[0])
	for c in coords:
		cur=countSight(coords, c, par)
		if len(cur)>len(best[0]):
			best=(cur, c)
	print(len(best[0]), best[1])
	order=[]
	for i in getDirection(coords, best[1]):

		if i[0] in best[0]:
			order.append(i[0])
	print(order[199])

