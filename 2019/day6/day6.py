class Planet(object):
	"""docstring for Planet"""
	def __init__(self, orbit):
		super(Planet, self).__init__()
		self.thingsInOrbit=[orbit]

	def addOrbit(plan):
		self.thingsInOrbit.append(plan)

	def __str__(self):
		return self.thingsInOrbit

	def __repr__(self):
		return str(self.thingsInOrbit)

def countOrbits(orbits, planet):
	total=0
	while planet in orbits:
		total+=1
		planet=orbits[planet]
	return total

def getAncestors(orbits, planet):
	ancestors=[]
	while planet in orbits:
		planet=orbits[planet]
		ancestors.append(planet)
	return ancestors

def findPathLen(lst1, lst2):
	while lst1[-1]==lst2[-1]:
		lst1.pop()
		lst2.pop()
	return len(lst1)+len(lst2)




# print(p.thingsInOrbit)
with open("input.txt", "r") as f:
	orbitDict={}

	for line in f:
		pair=line.strip().split(")")

		orbitDict[pair[1]]=pair[0]
	total=0
	for planet in orbitDict:
		total+=countOrbits(orbitDict, planet)
	# print(countOrbits(orbitDict, "C"))
		# Planet(pair[0])
	print(total)
	lst1=getAncestors(orbitDict, "YOU")
	lst2=getAncestors(orbitDict, "SAN")
	print(findPathLen(lst1, lst2))
		

