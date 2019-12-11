import sys
sys.path.append("..")
from intCode import Calculator

def getSize(panels):
	keys=list(panels.keys())
	maxx=max(map(lambda x: x[0], keys))
	maxy=max(map(lambda x: x[1], keys))
	minx=min(map(lambda x: x[0], keys))
	miny=min(map(lambda x: x[1], keys))
	# print("(", minx, miny, ") (",maxx, maxy,")")
	return ((minx, miny), (maxx, maxy))
	

inputArray=[3,8,1005,8,302,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,29,1006,0,78,2,1007,9,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,58,1006,0,7,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,83,2,1009,4,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,109,1,106,11,10,1006,0,16,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,138,2,108,0,10,1,101,14,10,1,1109,1,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,172,2,3,10,10,1006,0,49,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,201,1006,0,28,2,3,15,10,2,109,12,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,233,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,255,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,277,2,1107,9,10,101,1,9,9,1007,9,946,10,1005,10,15,99,109,624,104,0,104,1,21101,0,932856042280,1,21101,0,319,0,1105,1,423,21101,0,387512640296,1,21101,330,0,0,1106,0,423,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,46266346499,1,21102,1,377,0,1105,1,423,21102,1,46211836967,1,21102,1,388,0,1105,1,423,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,825460941588,1,21102,411,1,0,1106,0,423,21101,709475738388,0,1,21102,1,422,0,1105,1,423,99,109,2,21201,-1,0,1,21101,0,40,2,21102,454,1,3,21101,0,444,0,1106,0,487,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,449,450,465,4,0,1001,449,1,449,108,4,449,10,1006,10,481,1102,1,0,449,109,-2,2106,0,0,0,109,4,2102,1,-1,486,1207,-3,0,10,1006,10,504,21101,0,0,-3,22101,0,-3,1,21201,-2,0,2,21102,1,1,3,21102,1,523,0,1105,1,528,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,551,2207,-4,-2,10,1006,10,551,22101,0,-4,-4,1105,1,619,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,570,0,0,1106,0,528,22102,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,589,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,611,21201,-1,0,1,21101,611,0,0,106,0,486,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
c=Calculator(inputArray)
c.addInput(1)
positions=[(0,0)]
pos=(0,0)
colors={}
direction=0
while not c.finished:
	val1=c.calculate()
	val2=c.calculate()
	# print(val1, val2)
	colors[pos]=val1
	if val2 == 0:
		direction=(direction+3)%4
	else:
		direction=(direction+1)%4
	
	if direction==0:
		pos=(pos[0], pos[1]-1)
	elif direction==1:
		pos=(pos[0]+1, pos[1])
	elif direction==2:
		pos=(pos[0], pos[1]+1)
	elif direction==3:
		pos=(pos[0]-1, pos[1])
	# print(pos)
	positions.append(pos)
	if pos not in colors:
		colors[pos]=0
	c.addInput(colors[pos])
	


	

print(len(set(positions)))
picture=[["." for i in range(43)]for j in range(6)]
for panel in colors:
	print(panel)
	if colors[panel] == 1:
		picture[panel[1]][panel[0]]="#"
for i in picture:
	print("".join(i))

print(getSize(colors))