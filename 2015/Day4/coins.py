import md5
num=1
start="iwrupvqb"
while True:
	m=md5.new(start+str(num))
	if m.hexdigest()[0:6]=="000000":
		break
	else:
		num+=1
print num

