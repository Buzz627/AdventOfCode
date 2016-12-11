x1=0
y1=0
x2=0
y2=0
santa={str(x1)+","+str(y1):1}
robosanta={str(x2)+","+str(y2):1}
switch=0
with open("input.txt", "rb") as inputfile:
	for line in inputfile:
		for c in line:
			if switch==0:
				if c=="<":
					x1-=1
				elif c==">":
					x1+=1
				elif c=="^":
					y1+=1
				elif c=="v":
					y1-=1
				key=str(x1)+","+str(y1)
				if key not in santa:
					santa[key]=1
				else:
					santa[key]=santa[key]+1
				switch=1
			else:
				if c=="<":
					x2-=1
				elif c==">":
					x2+=1
				elif c=="^":
					y2+=1
				elif c=="v":
					y2-=1
				key=str(x2)+","+str(y2)
				if key not in santa:
					robosanta[key]=1
				else:
					robosanta[key]=santa[key]+1
				switch=0

for element in robosanta:
	if element in santa:
		santa[element]=santa[element]+robosanta[element]
	else:
		santa[element]=robosanta[element]
print len(santa)