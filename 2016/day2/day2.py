with open("input.txt", "rb") as inputfile:
	keypad=[[1,2,3],[4,5,6],[7,8,9]]
	newKeypad=[[0,0,1,0,0], [0,2,3,4,0],[5,6,7,8,9],[0,"A", "B", "C",0], [0,0,"D",0,0]]
	pos=[2, 0]
	password=""
	for line in inputfile:
		for i in line.strip():
			if i=="D" and pos[0]<4:
				pos[0]+=1
				if newKeypad[pos[0]][pos[1]] ==0:
					pos[0]-=1
				
			elif i=="L" and pos[1]>0:
				pos[1]-=1
				if newKeypad[pos[0]][pos[1]] ==0:
					pos[1]+=1
				
			elif i=="R" and pos[1]<4:
				pos[1]+=1
				if newKeypad[pos[0]][pos[1]] ==0:
					pos[1]-=1
				
			elif i=="U" and pos[0]>0:
				pos[0]-=1
				if newKeypad[pos[0]][pos[1]] ==0:
					pos[0]+=1
				
				
		password+=str(newKeypad[pos[0]][pos[1]])
		# print str(newKeypad[pos[0]][pos[1]])
	print password

		
		