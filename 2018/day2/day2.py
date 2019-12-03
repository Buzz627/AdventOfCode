def countLetters(word, n):
	for i in word:
		if word.count(i)==n:
			return True
	return False
def offByOne(word1, word2):
	flag=0
	for i in range(len(word1)):
		if word1[i]!=word2[i]:
			if flag==1:
				return False
			else:
				flag=1
	return True

two=0
three=0
words=[]
with open("input.txt") as f:
	for line in f:
		words.append(line)
		if countLetters(line, 2):
			two+=1
		if countLetters(line, 3):
			three+=1
	print "star1 {}".format(two*three)

for i in range(len(words)):
	for j in range(i+1, len(words)):
		if offByOne(words[i], words[j]):
			print words[i]
			print words[j]

