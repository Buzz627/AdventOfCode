
def findMax(dic):
	letter=""
	num=0
	for let in dic:
		if dic[let]>num:
			num=dic[let]
			letter=let
	return letter

def findMin(dic):
	letter=""
	num=float('infinity')
	for let in dic:
		if dic[let]<num:
			num=dic[let]
			letter=let
	return letter


with open("input.txt", "rb") as inputfile:
	firstLine=inputfile.next()
	transmition=[{}for k in range(len(firstLine.strip()))]
	for i in range(len(firstLine.strip())):
		transmition[i][firstLine[i]]=1

	for linea in inputfile:
		line=linea.strip()
		for i in range(len(line)):
			if line[i] not in transmition[i]:
				transmition[i][line[i]]=0
			transmition[i][line[i]]+=1
	ans=""
	for d in transmition:
		# print d
		ans+=findMin(d)
	print ans
