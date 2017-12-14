

firewall={}


def getPos(length, time):
	lst=range(length)+range(length-2, 0, -1)
	return lst[time%len(lst)]
def setsensors(firewall, time):
	sensors=[None]*(max(map(int, firewall.keys()))+1)
	for i in firewall:
		sensors[int(i)]=getPos(firewall[i], time)
	return sensors



with open("input.txt", "r") as f:
	for line in f:
		lst=line.strip().split(": ")
		firewall[lst[0]]=int(lst[1])
	# print firewall



	


wait=0
total=1
caught=1
while caught!=0:
	# sensors=setsensors(firewall, wait)
	# print sensors
	total=0
	caught=0
	for step in range(max(map(int, firewall.keys()))+1):
		
		# sensors=setsensors(firewall, wait+step)
		# print sensors
		# print step
		if str(step) in firewall:

			if getPos(firewall[str(step)], wait+step)==0:
				caught+=1
				total+=step*firewall[str(step)]
	# print total, "\n"
	wait+=1
print wait-1


# timeToWait=0
# while True:
# 	firewall=resetFirewall(firewall)
# 	print firewall
# 	for i in range(timeToWait):
# 		firewall=firewallStep(firewall)
# 	print firewall
# 	total=0
# 	counter=0
# 	for i in range(max(map(int, firewall.keys()))+1):

# 		if str(counter) in firewall:
# 			if firewall[str(counter)][1]==0:
# 				total+=counter*firewall[str(counter)][0]

# 		firewall=firewallStep(firewall)
# 		counter+=1
# 	print total
# 	if total==0:

# 		break
# 	timeToWait+=1
# 	# break

# print timeToWait