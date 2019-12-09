class Calculator():
	def __init__(self, startingProgram):
		self.startingProgram=startingProgram[::]
		self.program=startingProgram[::]
		self.pos=0
		self.paused=False
		self.inputs=[]
		self.inputNum=0
		self.finished=False
		self.output=0

	def addInput(self, num):
		self.inputs.append(num)

	def opCode(self, num):
		op=num%100
		result=[op]
		num=num//100
		for i in range(3):
			result.append(num%10)
			num=num//10

		return result

	def op1(self, op):

		a=self.program[self.pos+1]
		b=self.program[self.pos+2]
		res=self.program[self.pos+3]
		if op[1]==0:
			a=self.program[a]
		if op[2]==0:
			b=self.program[b]
		self.program[res]=a+b
		self.pos+=4

	def op2(self, op):
		a=self.program[self.pos+1]
		b=self.program[self.pos+2]
		res=self.program[self.pos+3]
		if op[1]==0:
			a=self.program[a]
		if op[2]==0:
			b=self.program[b]
		self.program[res]=a*b
		self.pos+=4

	def op3(self, op):
		# print(self.inputs)
		a=self.program[self.pos+1]
		self.program[a]=self.inputs[self.inputNum]
		self.inputNum+=1
		self.pos+=2
		

	def op4(self, op):
		a=self.program[self.pos+1]
		if op[1]==0:
			a=self.program[a]
		# print(a)
		output=a
		self.paused=True
		self.pos+=2
		self.output=output
		return output
		

	def op5(self, op):
		a=self.program[self.pos+1]
		b=self.program[self.pos+2]
		if op[1]==0:
			a=self.program[a]
		if op[2]==0:
			b=self.program[b]
		if a!=0:
			self.pos=b
		else:
			self.pos+=3

	def op6(self, op):
		a=self.program[self.pos+1]
		b=self.program[self.pos+2]
		if op[1]==0:
			a=self.program[a]
		if op[2]==0:
			b=self.program[b]
		if a==0:
			self.pos=b
		else:
			self.pos+=3
		

	def op7(self, op):
		a=self.program[self.pos+1]
		b=self.program[self.pos+2]
		res=self.program[self.pos+3]
		if op[1]==0:
			a=self.program[a]
		if op[2]==0:
			b=self.program[b]
		if a<b:
			self.program[res]=1
		else:
			self.program[res]=0
		self.pos+=4

	def op8(self, op):
		a=self.program[self.pos+1]
		b=self.program[self.pos+2]
		res=self.program[self.pos+3]
		if op[1]==0:
			a=self.program[a]
		if op[2]==0:
			b=self.program[b]
		if a==b:
			self.program[res]=1
		else:
			self.program[res]=0
		self.pos+=4

	def calculate(self):
		while self.program[self.pos]!=99:
			# print(self.pos)
			op=self.opCode(self.program[self.pos])
			if op[0]==1:
				self.op1(op)

			elif op[0]==2:
				self.op2(op)

			elif op[0]==3:
				self.op3(op)

			elif op[0]==4:
				return self.op4(op)

			elif op[0]==5:
				self.op5(op)

			elif op[0]==6:
				self.op6(op)

			elif op[0]==7:
				self.op7(op)

			elif op[0]==8:
				self.op8(op)

			else:
				print("error")
				break
		self.finished=True
		return self.output
