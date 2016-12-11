def vouls(word):
	count=0
	v=["a", "e", "i", "o", "u"]
	for c in word:
		if c in v:
			count+=1
		if count>=3:
			return True
	return False
def restrict(word):
	if "cd" in word:
		return True
	if "ab" in word:
		return True
	if "pq" in word:
		return True
	if "xy" in word:
		return True
def double(word):
	for i in range (0, len(word)-1):
		if word[i]==word[i+1]:
			return True
	return False

with open("input.txt", "rb") as inputfile:
	count=0
	for word in inputfile:
		if vouls(word) and double(word) and not restrict(word):
			count+=1
	print count

