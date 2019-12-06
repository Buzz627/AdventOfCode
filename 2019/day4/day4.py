def adjcentDigits(num):
	strNum=str(num)
	nums=[]
	i=0
	while i<len(strNum):
		current=strNum[i]
		temp=""
		# i+=1
		# if i >= len(strNum)-2:
			# break
		while i < len(strNum) and strNum[i]==current:
			# print(i, strNum[i])
			temp+=strNum[i]
			i+=1
		nums.append(temp)

	for l in nums:
		# print(l)
		if len(l)==2:
			return True
	return False




	# while i<len(strNum)-2

	# # for i in range(len(strNum)-2):
	# 	if strNum[i]==strNum[i+1]:
	# 		if strNum[i]!=strNum[i+2]:
	# 		return True
	# # print(num, "numbers")
	# return False

def decreses(num):
	strNum=str(num)
	for i in range(len(strNum)-1):
		if int(strNum[i])>int(strNum[i+1]):
			# print(num, "decreses")
			return True
	return False

def passing(num):
	return adjcentDigits(num) and not decreses(num)

print(passing(112233))
print(passing(123444))
print(passing(111122))

start=136818
end=685979
total=0
for i in range(start, end):
	if passing(i):
		total+=1
print(total)
