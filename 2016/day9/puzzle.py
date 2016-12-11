def getNums(code):
	nums=code.split("x")
	return map(int, nums)
def getdecompressedlen(text):
	totalLen=0
	start=0
	end=0
	while start<len(text):
		if text[start]=="(":
			end=start
			while text[end]!=")":
				end+=1
			n=getNums(text[start+1:end])
			end+=1
			l=getdecompressedlen(text[end:end+n[0]])
			l*=n[1]
			totalLen+=l
			start=end+n[0]-1

		else:
			if text[start] != " ":
				totalLen+=1
		start+=1
	return totalLen

def decompress(text):
	output=""
	part=""
	start=0
	end=0
	while start<len(text):
		if text[start]=="(":
			end=start
			while text[end]!=")":
				end+=1
			n=getNums(text[start+1:end])
			end+=1
			part=decompress(text[end:end+n[0]])


			part*=n[1]
			# print part
			# print text
			# print start
			# print end
			output+=part
			start=end+n[0]-1

		else:
			if text[start] != " ":
				output+=text[start]
		start+=1

	return output

with open("input.txt", 'rb') as inputfile:
	
	text=inputfile.next().strip()
	output=getdecompressedlen(text)
	print output
	# print len("XABCABCABCABCABCABCY")
