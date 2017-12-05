def isValid(phrase):
	newWords=[]
	words=phrase.split()
	for w in words:
		if w in newWords:
			return False
		newWords.append(w)
	return True
def isValidAnagram(phrase):
	newWords=[]
	words=phrase.split()
	for w in words:
		sortedWord=sortLetters(w)
		if sortedWord in newWords:
			return False
		newWords.append(sortedWord)
	return True

def sortLetters(word):
	return ''.join(sorted(word))



with open("input.txt","r") as f:
	star1=0
	star2=0
	for line in f:
		if isValid(line):
			star1+=1
		if isValidAnagram(line):
			star2+=1
	print star1
	print star2