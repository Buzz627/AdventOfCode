def getSeed(s):
	return s[-6:-1]

def getCounts(stri, seed):
	counts={}
	for s in seed:
		counts[s]=stri.count(s)
	return counts

def letterCounts(stri):
	counts={}
	for s in "".join(stri.split("-")):
		counts[s]=stri.count(s)
	return counts

def getstr(s):
	part=line.split("[")
	sen=part[0].split("-")
	sen.pop()
	return "-".join(sen)

def getID(s):
	part=s.split("[", 1)
	return part[0].split("-")[-1]

def insert(lst, item):
	if lst.isempty():
		lst.append(item)
		return
	i=0
	while i<len(lst):
		cur=lst[0]
		if item[0]>cur[0]:
			lst.insert(i, item)
			return
		i+=1

	lst.insert(i, item)

def rotate(s, num):
	res=[""]*len(s)
	for i in range(len(s)):
		if s[i]=="-":
			res[i]=" "
			continue
		a=ord(s[i])-97
		a+=num
		a%=26
		res[i]=chr(a+97)
	return "".join(res)

def isMostComon(seed, stri):
	counts=letterCounts(stri)

	revCounts={}
	for i in counts:
		if counts[i] not in revCounts:
			revCounts[counts[i]]=[]
		revCounts[counts[i]].append(i)
		revCounts[counts[i]].sort()
	nums=revCounts.keys()
	nums.sort(reverse=True)
	letters=""
	for i in nums:
		for j in revCounts[i]:
			letters+=j
	return seed==letters[0:5]
	


def isgood(seed, counts):
	last=count[seed[0]]
	for i in range(1, 5):
		cur=count[seed[i]]
		# print last, cur
		if cur>last:
			
			return False
		elif cur==last:
			if seed[i]<seed[i-1]:
				return False
		last=cur
	return True



with open("input.txt", "rb") as inputfile:
	total=0
	
	for line in inputfile:
		seed=getSeed(line.strip())
		roomid=getID(line.strip())
		name=getstr(line.strip())
		count=getCounts(name, seed)
		print rotate(name, int(roomid)), roomid
		if isgood(seed, count) and isMostComon(seed, name):
			# print name
			total+=int(roomid)
	print total
		


