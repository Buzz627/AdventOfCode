def double(word):
	for i in range (0, len(word)-2):
		if word[i]==word[i+2]:
			return True
	return False
def pairs(word):
	for i in range(0, len(word)-2):
		pair=word[i:i+2]
		if pair in word[i+2:len(word)+1]:
			return True
	return False

with open("input.txt", "rb") as inputfile:
	count=0
	for word in inputfile:
		if pairs(word) and double(word):
			count+=1
	print count
print pairs("aaaa") 
print double("uurcxstgmygtbstg")
