
import math
class Reaction():
	def __init__(self, createdAmount, requirements):
		self.createdAmount=createdAmount
		self.requirements=requirements

	def __repr__(self):
		return str(self.requirements)+ " => " + str(self.createdAmount)

reactions={}
leftOver={}
def create(chemical, amount):
	global reactions
	print(chemical, amount)
	if chemical=="ORE":
		return amount

	total=0

	r=reactions[chemical]

	for key in r.requirements:
		
		temp=create(key, r.requirements[key])* math.ceil(amount/r.createdAmount)
		total+=temp
	return total


with open("input.txt", "r") as f:
	
	for line in f:
		parts=line.strip().split(" => ")
		requirementLst=parts[0].strip().split(", ")
		requirements={}
		for i in requirementLst:
			n=i.split(" ")[1]
			num=int(i.split(" ")[0])
			requirements[n]=num

		result=parts[1].strip()

		name=result.split(" ")[1]
		reactions[name]=Reaction(int(result.split(" ")[0]), requirements)
		# print(reactions[name], name)

	print("needed", create("C", 1))