import re

def getABA(s):
	res=[]
	for i in range(len(s)):
		part=s[i:i+3]
		if len(part)==3 and part==part[::-1]:
			res.append(s[i+1]+s[i]+s[i+1])
	return res


def ssl(s, corr):
	for i in range(len(s)):
		part=s[i:i+3]
		if len(part)==3 and part==part[::-1]:
			if part in corr:
				return True
	return False



def pair(s):
	for i in range(len(s)):
		if s[i:i+2]==s[i+3:i+1:-1]:
			if s[i]!=s[i+1]:
				return True
	return False


with open("input.txt", "rb") as inputfile:
	count=0
	for line in inputfile:
		lst=re.split(r"[\[\]]", line.strip())
		seq=[0,0]
		aba=[]
		for s in range(0, len(lst), 2):
		# 	if pair(lst[s]):
		# 		seq[s%2]+=1
		# 	ssl=getABA()
		# if seq[0]>0 and seq[1]==0:
			aba.extend(getABA(lst[s]))
		for s in range(1, len(lst), 2):
			if ssl(lst[s], aba):
				count+=1
				break
	print count
		