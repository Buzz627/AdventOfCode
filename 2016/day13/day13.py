class Node:
	def __init__(self, x, y, parent):
		self.x=x
		self.y=y
		self.parent=parent
		if parent==None:
			self.steps=0
		else:
			self.steps=parent.steps+1



def isOpen(x, y, num):
	t=x*x + 3*x + 2*x*y + y + y*y + num
	b=map(int, list(bin(t)[2:]))
	if sum(b)%2==0:
		return True
	return False

def getMoves(x, y):
	moves=[]
	favnum=1350
	# favnum=10
	if isOpen(x+1, y, favnum):
		moves.append((x+1, y))
	if isOpen(x-1, y, favnum):
		moves.append((x-1, y))
	if isOpen(x, y+1, favnum):
		moves.append((x, y+1))
	if isOpen(x, y-1, favnum):
		moves.append((x, y-1))
	return moves

goal=(31,39)
start=Node(1, 1, None)
openlst=[start]
closedlst=[]
spaces=[]
while len(openlst)>0:
	cur=openlst.pop(0)
	
	if cur.steps>50:
		break
	# if (cur.x, cur.y)==goal:
	# 	end=cur
	# 	break
	elif cur.steps<=50: 
		spaces.append((cur.x, cur.y))

	for m in getMoves(cur.x, cur.y):
		if m[0]>=0 and m[1]>=0:
			if m not in closedlst:
				openlst.append(Node(m[0], m[1], cur))
				closedlst.append(m)
			
count=0
# cur=end
# while cur!=None:
# 	count+=1
# 	cur=cur.parent
# print count-1
# print cur.steps, cur.x, cur.y
print len(set(closedlst))-1
print len(set(spaces))
# print spaces
for y in range (5):
	for x in range(5):
		if isOpen(x, y, 1350):
			print ".",
		else: print "#",
	print ""



