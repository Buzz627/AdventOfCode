class Moon():
	def __init__(self, x,y,z):
		self.pos=[x,y,z]
		self.x=x
		self.y=y
		self.z=z

		self.velocity=[0,0,0]
		self.vx=0
		self.vy=0
		self.vz=0

	def updatePos(self):
		for i in range(3):
			self.pos[i]+=self.velocity[i]

	def updateAxis(self, axis):
		setattr(self, axis, getattr(self, axis)+getattr(self, "v"+axis))
		


	def updateVAxis(self, moon, axis):

		if getattr(self, axis) > getattr(moon, axis):
			setattr(self, "v"+axis,
				getattr(self, "v"+axis)-1)
		if getattr(self, axis) < getattr(moon, axis):
			setattr(self, "v"+axis,
			getattr(self, "v"+axis)+1)

	def updateVelocity(self, moon):
		for i in range(3):

			if self.pos[i] > moon.pos[i]:
				self.velocity[i]-=1
			elif self.pos[i] < moon.pos[i]:
				self.velocity[i]+=1

	def getPotential(self):
		return sum(map(lambda x: abs(x), self.pos))

	def getKinetic(self):
		return sum(map(lambda x: abs(x), self.velocity))

	def getTotalEnergy(self):
		return self.getKinetic()*self.getPotential()

def step(moons):
	for i in range(len(moons)):
		for j in range(len(moons)):
			if i==j:
				continue
			else:
				moons[i].updateVelocity(moons[j])

	for m in moons:
		m.updatePos()

def stepAxis(moons, axis):
	for i in range(len(moons)):
		for j in range(len(moons)):
			if i==j:
				continue
			else:
				moons[i].updateVAxis(moons[j], axis)

	for m in moons:
		m.updateAxis(axis)


def universeState(moons, axis):
	state=[]
	for m in moons:
		state.append(getattr(m, axis))
		state.append(getattr(m, "v"+axis))
	return tuple(state)




#example1

# a=Moon(x=-1, y=0, z=2)
# b=Moon(x=2, y=-10, z=-7)
# c=Moon(x=4, y=-8, z=8)
# d=Moon(x=3, y=5, z=-1)



#example2

a=Moon(x=-8, y=-10, z=0)
b=Moon(x=5, y=5, z=10)
c=Moon(x=2, y=-7, z=3)
d=Moon(x=9, y=-8, z=-3)

#input
a=Moon(x=6, y=-2, z=-7)
b=Moon(x=-6, y=-7, z=-4)
c=Moon(x=-9, y=11, z=0)
d=Moon(x=-3, y=-4, z=6)


moons=[a,b,c,d]



# for i in range(1000):
# 	step(moons)

# print(sum(map(lambda x: x.getTotalEnergy(), moons)))
results=[]
for axis in ["x", "y", "z"]:
	universe=set()
	steps=0
	state=universeState(moons, axis)
	while state not in universe:
		universe.add(state)
		# print(state)
		stepAxis(moons, axis)
		state=universeState(moons, axis)
		
		steps+=1
	# print(universe)
	print(steps)
	results.append(steps)
	





