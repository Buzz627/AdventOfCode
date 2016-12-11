import csv
with open('input.txt', 'rb') as inputFile:
	csvfile=csv.reader(inputFile, delimiter='x')
	paperTotal=0
	ribbonTotal=0
	for line in csvfile:
		l=int(line[0])
		w=int(line[1])
		h=int(line[2])
		x=l*w
		y=l*h
		z=w*h
		ribbon=(2*l)+(2*w)+(2*h)
		ribbon-=(2*max(l,w,h))
		paperTotal+=((2*(x+y+z))+min(x, y, z))
		ribbonTotal+=(ribbon+(l*w*h))
print "paper", paperTotal
print "ribbon", ribbonTotal
