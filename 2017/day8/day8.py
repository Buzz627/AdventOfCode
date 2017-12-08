
def compare(a, symbol, b):
	if symbol=="==":
		return a==b
	if symbol=="!=":
		return a!=b
	if symbol==">=":
		return a>=b
	if symbol=="<=":
		return a<=b
	if symbol==">":
		return a>b
	if symbol=="<":
		return a<b

registers={}
star2=0
with open("input.txt","r")as f:
	for line in f:
		lst=line.split()
		# print lst
		if lst[0] not in registers:
			registers[lst[0]]=0
		if lst[4] not in registers:
			registers[lst[4]]=0
		if compare(registers[lst[4]], lst[5], int(lst[6])):
			if lst[1]=="inc":
				registers[lst[0]]+=int(lst[2])
			elif lst[1]=="dec":
				registers[lst[0]]-=int(lst[2])
		if registers[lst[0]]>star2:
			star2=registers[lst[0]]

star1=0
for i in registers:
	if registers[i]>star1:
		star1=registers[i]
print star1
print star2