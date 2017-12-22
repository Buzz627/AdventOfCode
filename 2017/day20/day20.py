x=0
y=1
z=2
class Particle:
	
	def __init__(self, p, v, a, num):
		self.id=num
		self.pos=map(int, p.split(','))
		self.vel=map(int, v.split(','))
		self.acc=map(int, a.split(','))
		self.destroyed=False

	def __repr__(self):
		return ("ID  "+str(self.id)+
		"\ndis "+str(self.getDistance())+
		"\nacc "+str(self.getAccl())+"\n"+
		str(self.pos)+"\n"+
		str(self.vel)+"\n"+
		str(self.acc)+
		"\ndes "+str(self.destroyed))

	def update(self):
		self.updateSpeed()
		self.updatePos()

	def updateSpeed(self):
		self.vel[x]+=self.acc[x]
		self.vel[y]+=self.acc[y]
		self.vel[z]+=self.acc[z]

	def updatePos(self):
		self.pos[x]+=self.vel[x]
		self.pos[y]+=self.vel[y]
		self.pos[z]+=self.vel[z]


	def getDistance(self):
		return abs(self.pos[x])+abs(self.pos[y])+abs(self.pos[z])

	def getAccl(self):
		return abs(self.acc[x])+abs(self.acc[y])+abs(self.acc[z])



# text=["p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>", "p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"]
# text=["p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>",
# "p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>",
# "p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>",
# "p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>"]
particles=[]
num=0
with open("input.txt", "r") as text:
	for part in text:
		lst=part.strip().split(", ")
		p=lst[0][3:-1]
		v=lst[1][3:-1]
		a=lst[2][3:-1]
		particles.append(Particle(p, v, a, num))
		num+=1

closest=0
clDist=particles[0].getDistance()


best=2
for p in particles:
	a=p.getAccl()
	# print a
	if a==best:
		best=a
		bestpart=p
		print p




ticks=0

while ticks<10000:
	positions={}
	for p in particles:
		if not p.destroyed:
			p.updateSpeed()
			p.updatePos()
			if tuple(p.pos) not in positions:
				positions[tuple(p.pos)]=[]
			positions[tuple(p.pos)].append(p.id)
	for pos in positions:
		if len(positions[pos])>1:
			for i in positions[pos]:
				particles[i].destroyed=True



	ticks+=1


count=0

for p in particles:
	# print p
	if not p.destroyed:
		count+=1
print ""
print count




	

