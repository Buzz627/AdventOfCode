import json
test='''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''.split('\n')
class Node(object):
	"""docstring for Node"""
	def __init__(self, name, weight):
		super(Node, self).__init__()
		self.name = name
		self.children=[]
		self.weight=weight
		self.heldweight=0
	def addChild(self, child):
		self.children.append(child)
	def __str__(self):
		return json.dumps({"name":self.name, "weight":self.weight, "heldweight":self.heldweight, "children":self.children})
	__repr__ = __str__



nodes={}
lines=[]
def height(key):
	if len(nodes[key].children)==0:
		return 1
	maxHeight=0
	for c in nodes[key].children:
		h=height(c)
		if h>maxHeight:
			maxHeight=h
	return 1+maxHeight

def updateWeights(key):
	if len(nodes[key].children)==0:
		nodes[key].heldweight=0
		return
	total=0
	for c in nodes[key].children:
		updateWeights(c)
		total+=nodes[c].weight+nodes[c].heldweight

	nodes[key].heldweight=total

def compareWeight(key):
	if len(nodes[key].children)==0:
		return 
	current=nodes[key].children[1]
	value=nodes[current].weight+nodes[current].heldweight
	for c in nodes[key].children:
		compareWeight(c)
		if nodes[c].weight+nodes[c].heldweight != value:
			print value, nodes[c].weight, nodes[c].heldweight, c, value-nodes[c].heldweight, key
			print value, nodes[current].weight, nodes[current].heldweight, current, value-nodes[current].heldweight, key
			print ""





with open("input.txt","r") as f:
	for line in f:
		line=line.strip("\n")
		lst=line.split(" ", 3)
		nodes[lst[0]]= Node(lst[0], int(lst[1].strip("()")))
		if len(lst)>2:
			for child in lst[3].split(", "):
				nodes[lst[0]].addChild(child)



maxHeight=0
maxNode=""
for i in nodes:
	# print nodes[i]
	current=height(i)
	if current>maxHeight:

		maxHeight=current
		maxNode=i
	# print current, i
print ""
print maxHeight
print maxNode
updateWeights(maxNode)
compareWeight(maxNode)
print ""
# for i in ["utlqx", "xzhdy", "tlmvaep", "nbyij", "fszyth", "zimrf"]:
# 	print nodes[i].weight+nodes[i].heldweight, i



		