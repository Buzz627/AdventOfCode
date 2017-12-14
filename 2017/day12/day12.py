graph={}
groups=[]
def findGroup(num):
	closed=[]
	stack=[num]
	while len(stack)>0:
		current=stack.pop()
		for i in graph[str(current)]:
			if i not in closed:

				stack.append(i)
				closed.append(i)
		
	return closed


with open("input.txt", "r")as f:
	for line in f:
		current=line.strip().split(" ", 2)
		# print current
		graph[current[0]]=map(int, current[2].split(', '))

count=0
closed=[]
stack=[0]
while len(stack)>0:
	current=stack.pop()
	for i in graph[str(current)]:
		if i not in closed:
			count+=1
			stack.append(i)
			closed.append(i)
	
print closed

for i in graph:
	g=findGroup(i)
	if tuple(sorted(g)) not in groups:
		groups.append(tuple(sorted(g)))
print len(groups)




		
