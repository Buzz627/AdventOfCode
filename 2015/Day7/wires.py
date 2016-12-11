import csv
import copy
t={}
answers={}
# print ~1
with open("input.txt", "rb") as inputFile:
	csvfile=csv.reader(inputFile, delimiter=' ')
	for function in csvfile:
		# print function
		if "NOT" in function:
			x=function[0:2]
			# x=lambda: ~t[function[1]]()
		elif "OR" in function:
			x=function[0:3]
			# x=lambda:t[function[0]]()|t[function[2]]()
		elif "AND" in function:
			x=function[0:3]
			# x=lambda:t[function[0]]()&t[function[2]]()
		elif "LSHIFT" in function:
			x=function[0:3]
			# x=lambda:t[function[0]]()<<int(function[2])
		elif "RSHIFT" in function:
			x=function[0:3]
			# x=lambda:t[function[0]]()>>int(function[2])
		else:
			x=function[0]
			# answers[function[len(function)-1]]=x
		
		t[function[len(function)-1]]=x


for i in range(0, len(t)):
# while 'a' not in answers:
	for key in t:
		function=t[key]
		if len(function)>1:
			print function
			if "NOT" in function:
				if function[1] in answers:
					x= ~int(answers[function[1]])
			else:
				if "OR" in function:
					if function[0] in answers and function[2] in answers:
						x=int(answers[function[0]])|int(answers[function[2]])
				elif "AND" in function:
					if function[0] in answers and function[2] in answers:
						x=int(answers[function[0]])&int(answers[function[2]])
				elif "LSHIFT" in function:
					if function[0] in answers:
						x=int(answers[function[0]])<<int(function[2])
				elif "RSHIFT" in function:
					if function[0] in answers:
						x=int(answers[function[0]])>>int(function[2])
			t[key]=[x]
			answers[key]=x

print t.keys()
print t
print t['a']
print answers.keys()
#b=0
#c=3
#d=b+c
#a=d+2