class Bot:
	def __init__(self, n):
		self.num=n
		self.chips=[]
		self.rules={"high":None,"low": None}

	def addChip(self, num):
		self.chips.append(num)

	def removeChip(self, num):
		self.chips.remove(num)

	def applyRule(self):
		if len(self.chips)==2:
			if max(self.chips) ==61 and min(self.chips)==17:
				print self.num
			res=[(self.rules["high"], max(self.chips)), (self.rules["low"], min(self.chips))]
			self.chips=[]
			return res
		return None

with open("input.txt", 'rb')as inputfile:
	bots={}
	outputs={}
	for line in inputfile:
		line=line.split()
		if len(line)==6:
			if int(line[5]) not in bots:
				bots[int(line[5])]=Bot(int(line[5]))
			bots[int(line[5])].addChip(int(line[1]))
		if len(line)==12:
			if int(line[1]) not in bots:
				bots[int(line[1])]=Bot(int(line[1]))
			bots[int(line[1])].rules[line[3]]=line[5:7]
			bots[int(line[1])].rules[line[8]]=line[10:12]
			
	
	while True:
		tasks=[]
		for i in bots:
			# print i, bots[i].chips, bots[i].rules
			t=bots[i].applyRule()
			if t!=None:
				tasks.extend(t)
		if len(tasks)==0:
			break
		for t in tasks:
			if t[0][0]=="bot":
				bots[int(t[0][1])].addChip(t[1])
			if t[0][0]=="output":
				outputs[int(t[0][1])]=t[1]
	print outputs
	total=1
	for i in range(3):
		total*=outputs[i]
	print total


