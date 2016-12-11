import csv
class Light:
	def __init__(self):
		self.power=False
	def turnOn(self):
		self.power=True
	def turnOff(self):
		self.power=False
	def toggle(self):
		if self.power:
			self.power=False
		else:
			self.power=True

grid=[[0 for x in range(1000)] for x in range(1000)] 

with open("input.txt", "rb") as inputFile:
	csvfile=csv.reader(inputFile, delimiter=' ')
	# x=0
	# for i in range(0, 3):
	# 	for j in range(0, 3):
	# 		grid[j][i]=True
			

	for line in csvfile:
		if len(line)>4:
			line.pop(0)
		command=line[0]
		start=line[1].split(",")
		end=line[3].split(",")
		for i in range(int(start[0]), int(end[0])+1):
			for j in range(int(start[1]), int(end[1])+1):
				if command=="on":
					grid[i][j]+=1
				elif command=="off":
					if grid[i][j]>0:
						grid[i][j]-=1
				elif command=="toggle":
					grid[i][j]+=2
					# if grid[i][j]==1:
					# 	grid[i][j]=0
					# else:
					# 	grid[i][j]=1

total=0
for i in range(0, 1000):
	for j in range (0, 1000):
		total+=grid[i][j]
print total
# for i in range(0, 1000):
# 	print grid[i][0]
# print grid[0]



