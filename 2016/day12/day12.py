with open("input.txt","rb") as inputfile:
	instructions=[]
	registers={"a":0, "b":0,"c":1}
	for line in inputfile:
		instructions.append(line.split())
	i=0
	while i<len(instructions):
		curr=instructions[i]
		if curr[0]=="cpy":
			if curr[1].isdigit():
				registers[curr[2]]=int(curr[1])
			else:
				registers[curr[2]]=registers[curr[1]]
		
		if curr[0]=="inc":
			registers[curr[1]]+=1
		if curr[0]=="dec":
			registers[curr[1]]-=1
		if curr[0]=="jnz":
			if curr[1].isdigit():
				val=int(curr[1])
			else:
				val=registers[curr[1]]

			if val!=0:
				i+=int(curr[2])-1
		
		i+=1
	print registers