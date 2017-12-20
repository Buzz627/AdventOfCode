
def getMiddle(directions):
	first=False
	combos=[['n','nw','ne'],['s','se','sw'],['ne','se','n'],['nw','sw','n'],['sw','nw','s'],['se','ne','s']]
	found=0
	for c in combos:
		if sorted(c)==sorted(directions):
			return c[0]

	

def getDistance(directions):
	#n=nw+ne
	#s=se+sw
	#ne=se+n
	#nw=sw+n
	#sw=nw+s
	#se=ne+s

	threeDir={}
	
	pairs=[("n", "s"), ("nw", "se"), ("ne", "sw")]
	for p in pairs:
		if directions[p[0]]>directions[p[1]]:
			threeDir[p[0]]=directions[p[0]]-directions[p[1]]
		else:
			threeDir[p[1]]=directions[p[1]]-directions[p[0]]
	print threeDir
	formula=getMiddle(threeDir.keys())
	print formula
	
	

	return 





commands={"n":0,"nw":0,"ne":0}
x=0
y=0

# test="se,sw,se,sw,sw,n"
# test="ne,ne,ne"
test="se,n,sw,ne,n,n,n,se,nw,nw,nw,sw,sw"
# test="ne,se,ne,se"
maxDist=0
with open ("input.txt", "r") as f:
	for line in f:
		lst=line.split(",")
		for i in lst:
			
			if i not in commands:
				commands[i]=0
			commands[i]+=1
			if i=="n":
				y+=1
			if i=="s":
				y-=1
			if i=="nw":
				x-=1
			if i=="sw":
				x-=1
				y-=1
			if i=="ne":
				x+=1
				y+=1
			if i=="se":
				x+=1
			if (abs(x)+abs(y)+abs(x-y))/2>maxDist:
				maxDist=(abs(x)+abs(y)+abs(x-y))/2

			# north=commands["n"]-commands["s"]
			# northeast=(commands["ne"]-commands["sw"])
			# northwest=(commands["nw"]-commands["se"])
			# if abs(north)+abs(northeast)+abs(northwest)>maxDist[0]:
			# 	maxDist=(abs(north)+abs(northeast)+abs(northwest),north, northeast, northwest)

print x, y, y-x, (abs(x)+abs(y)+abs(x-y))/2

total=0

# north=((commands["n"]+abs(commands["ne"]-commands["nw"]))-(commands["s"]+abs(commands["se"]-commands["sw"])))
# north=commands["n"]-commands["s"]
# northeast=(commands["ne"]-commands["sw"])
# northwest=(commands["nw"]-commands["se"])

# print north, northeast,northwest


print maxDist

exit()

# print ((861-311)+658+311)
print ((406-19)+418+19)

# print commands

# south=min(commands["sw"], commands["se"])+commands["s"]

north=min(commands["nw"], commands["ne"])+commands["n"]



west=max(commands["sw"],commands["nw"])-(max(commands["sw"],commands["nw"])-min(commands["sw"],commands["nw"]))
east=max(commands["se"],commands["ne"])-(max(commands["se"],commands["ne"])-min(commands["se"],commands["ne"]))

for i in commands:
	print i, commands[i]
# print north, south, west, east
# print abs(north-south)+abs(west-east)


# side=(max(northwest, northeast)-min(northwest, northeast))
# print side
# north+=side
# print north, max(northwest, northeast)-side

# print max(north, northwest, northeast)-min(north, northwest, northeast)

