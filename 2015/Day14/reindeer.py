class reindeer:
	def __init__(self, name, speed, duration, rest):
		self.name=name
		self.speed=speed
		self.rest=rest
		self.duration=duration
		self.resting=False
		self.step=0
		self.distance=0
	def race(self, time):
		x=self.duration+self.rest
		self.distance=(time/x)*(self.speed*self.duration)
		y=time%x
		if y>self.duration:
			self.distance+=self.speed*self.duration
		else:
			self.distance+=self.speed*y
	



comet=reindeer("comet", 14, 10, 127)
dancer=reindeer("dancer", 16, 11, 162)
comet.race(1000)
dancer.race(1000)
print comet.distance
print dancer.distance

with open("input.txt", "rb")as inputfile:
	racers=[]
	for line in inputfile:
		t=line.split(" ")
		racers.append(reindeer(t[0], int(t[3]), int(t[6]), int(t[13])))
	for deer in racers:
		deer.race(2503)
		print deer.name, deer.distance

