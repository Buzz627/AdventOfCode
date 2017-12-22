text=[]
# text=[	"..#",
# 		"#..",
# 		"..."]


infected={}
direction=0
with open("input.txt", "r") as f:
	for line in f:
		text.append(line.strip())
for l in text:
	print l
for y in range(len(text)):
	for x in range(len(text[y])):
		if text[y][x]=="#":
			infected[(x, y)]='infected' 
posx=len(text)/2
posy=len(text[posx])/2
star2=0
for i in range (10000000):
	if (posx, posy) in infected:
		if infected[(posx, posy)]=="infected":
			direction=(direction+1)%4
			infected[(posx, posy)]="flagged"

		elif infected[(posx, posy)]=="weak":
			infected[(posx, posy)]="infected"
			star2+=1

		elif infected[(posx, posy)]=="flagged":
			direction=(direction+2)%4
			del infected[(posx, posy)]
		

	else:
		direction=(direction-1)%4
		infected[(posx, posy)]="weak"
	# print infected

	if direction==0:
		posy-=1
	if direction==1:
		posx+=1
	if direction==2:
		posy+=1
	if direction==3:
		posx-=1

# print infected
print star2
