import csv
x=0
y=0
maxPos=0
a=[]
b=[]
test="Up, Up, Down, Down, Left, Right, Left, Right, B, A, Start"

def dist(a, b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

def maxDist(a, b):
	maxpos=0
	for i in a:
		for j in b:
			maxpos=max(dist(i, j), maxpos)
	return maxpos


with open("elvish_cheat_codes.txt", "r") as f:

	reader = csv.reader(f, delimiter=',')
	for i in reader:
		commands=map(lambda x:x.strip(), i)
	# commands="Up, A, Right, Right, B, Left, B, Start".split(", ")
	print commands
	for c in commands:
		if c=="Down":
			y-=1
		elif c=="Up":
			y+=1
		elif c=="Right":
			x+=1
		elif c=="Left":
			x-=1
		elif c=="A":
			maxPos=max(maxPos, dist((0, 0), (x, y)))
			a.append((x, y))
		elif c=="B":
			maxPos=max(maxPos, dist((0, 0), (x, y)))
			b.append((x, y))
		elif c=="Start":
			break
		else:
			print "problem"
	print dist((1,2) , (8,6))
	print a
	print b
	print maxPos
	print maxDist(a, b)


		