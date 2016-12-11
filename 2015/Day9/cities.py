import heapq
with open("input.txt", "rb")as inputfile:
	nodes={}
	edges={}
	for x in inputfile:
		line=x.strip().split(" ")
		nodes[line[0]]=0
		nodes[line[2]]=0
		if line[0] not in edges:
			edges[line[0]]=[]
		heapq.heappush(edges[line[0]],(int(line[4]), line[2]))
		if line[2] not in edges:
			edges[line[2]]=[]
		heapq.heappush(edges[line[2]],(int(line[4]), line[0]))
smallest=588

for city in nodes:
	visited=[]
	next=0
	while True:
		current=edges[city][0]
		if current[1] in visited:
			next+=1
		if next>=len(edges[city]):
			

	



# start='Straylight'
# nodes[start]=1
# h=[]
# for element in edges[start]:
# 	heapq.heappush(h, element)
# total=0
# while len(h)>0:
# 	current=h.pop(0)
# 	if nodes[current[1]]==0:
# 		total+=current[0]
# 		nodes[current[1]]=1
# 		for element in edges[current[1]]:
# 			heapq.heappush(h, element)
# print total



