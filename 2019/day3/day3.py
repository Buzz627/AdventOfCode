def distanceFromStart(point):
	return abs(point[0])+abs(point[1])

def makePath(instructions):
	points={(0,0):0}
	current=(0,0)
	steps=1
	for i in instructions:
		direction=i[0]
		distance=int(i[1:])
		if direction=="U":
			for j in range(current[1]+1, current[1]+1+distance):
				points[(current[0], j)]=steps
				steps+=1
			current=(current[0], j)
		if direction=="D":
			for j in range(current[1]-1, current[1]-1-distance, -1):
				points[(current[0], j)]=steps
				steps+=1
			current=(current[0], j)
		if direction=="R":
			for j in range(current[0]+1, current[0]+1+distance):
				points[(j, current[1])]=steps
				steps+=1
			current=(j, current[1])
		if direction=="L":
			for j in range(current[0]-1, current[0]-1-distance, -1):
				points[(j, current[1])]=steps
				steps+=1
			current=(j, current[1])

	return points

def findMatches(points1, points2):
	matches=[]

	for p in points1:
		if p == (0,0):
			continue
		if p in points2:
			matches.append((p, points1[p], points2[p]))
	return matches

def findClosest(matches):
	best=(float('inf'),(0,0))
	for m in matches:
		distance= distanceFromStart(m[0])
		if distance<best[0]:
			best=(distance, m)
	return best

def findShortest(matches):
	best=(float('inf'),(0,0))
	for m in matches:
		distance=m[1]+m[2]
		if distance<best[0]:
			best=(distance, m)
	return best


with open("input.txt", "r") as f:

	instructions1=["R8","U5","L5","D3"]
	instructions2=["U7","R6","D4","L4"]
	instructions1=f.readline().strip().split(",")
	instructions2=f.readline().strip().split(",")

	points1=makePath(instructions1)
	print("found path1")
	points2=makePath(instructions2)
	print("found path2")
	matches=findMatches(points1, points2)
	print("found matches")

	print(findClosest(matches))
	print(findShortest(matches))




