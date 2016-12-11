registers={"a":0, "b":0}
def dostep(ins, reg, current, jmp):
	if ins=="inc":
		registers[reg]=registers[reg]+1
	if ins=="tpl":
		registers[reg]=registers[reg]*3
	if ins=="hlf":
		registers[reg]=registers[reg]/2
	if ins=="jmp":
		return reg
	if ins=="jie":
		if registers[reg]%2==0:
			if jmp[0]=="+":
				return 
	if ins=="jio":
		if registers[reg]==1:
			return jmp


	return current+1


with open("input.txt", "rb") as inputfile:
	instructions={}
	step=0
	for line in inputfile:
		instructions[step]=line.strip()
		step+=1
print instructions
x=0
while x<47:
	temp=instructions[x].split(' ')
	if len(temp)>2:
		x=

