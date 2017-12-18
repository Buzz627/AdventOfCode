txt='''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''
# txt='''set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2'''
reg0={"p":0}
reg1={"p":1}
p0input=[]
p1input=[]
p0counter=0
p1counter=0
commands=[]
lastPlayed=0


def getValue0(val):
	try: 
		return int(val)
	except:
		return reg0[val]


def getValue1(val):
	try: 
		return int(val)
	except:
		return reg1[val]



with open("input.txt", "r") as f:
	# for line in txt.split('\n'):
	for line in f:
		lst=line.strip().split()
		commands.append(lst)
		# print lst
# print commands
star2=0
while True:

	while p0counter<len(commands):
		# print p0counter
		lst=commands[p0counter]
		if lst[1]not in reg0:
			reg0[lst[1]]=0
		if lst[0]=="add":
			reg0[lst[1]]=reg0[lst[1]]+getValue0(lst[2])
			
		if lst[0]=="mul":
			reg0[lst[1]]=reg0[lst[1]]*getValue0(lst[2])
		if lst[0]=="set":
			reg0[lst[1]]=getValue0(lst[2])
		if lst[0]=="mod":
			reg0[lst[1]]=reg0[lst[1]]%getValue0(lst[2])
		if lst[0]=="snd":
			p1input.append(getValue0(lst[1]))
		if lst[0]=="rcv":
			if len(p0input)>0:
				reg0[lst[1]]=p0input.pop(0)
			else:
				break
		if lst[0]=="jgz":
			if getValue0(lst[1]) >0:
				p0counter+= getValue0(lst[2])
				continue
		
		p0counter+=1


	while p1counter<len(commands):
		# print p0counter
		lst=commands[p1counter]
		if lst[1]not in reg1:
			reg1[lst[1]]=0
		if lst[0]=="add":
			reg1[lst[1]]=reg1[lst[1]]+getValue1(lst[2])
			
		if lst[0]=="mul":
			reg1[lst[1]]=reg1[lst[1]]*getValue1(lst[2])
		if lst[0]=="set":
			reg1[lst[1]]=getValue1(lst[2])
		if lst[0]=="mod":
			reg1[lst[1]]=reg0[lst[1]]%getValue1(lst[2])
		if lst[0]=="snd":
			star2+=1
			p0input.append(getValue1(lst[1]))
		if lst[0]=="rcv":
			if len(p1input)>0:
				reg1[lst[1]]=p1input.pop(0)
			else:
				break
		if lst[0]=="jgz":
			if getValue1(lst[1]) >0:
				p1counter+= getValue1(lst[2])
				continue
		
		p1counter+=1


	print p1input, p0input
	if len(p1input)==0 and len(p0input)==0:
		break
print star2
	# print lst