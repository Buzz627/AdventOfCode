class Calculator():
	def __init__(self, startingProgram, inputType="continuous", base=0):
		self.startingProgram=startingProgram[::]
		self.program=startingProgram[::]
		self.pos=0
		self.paused=False
		self.inputs=[]
		self.inputNum=0
		self.finished=False
		self.output=0
		self.base=base
		self.convertToDict()
		self.inputType=inputType
		
	def isFinished(self):
		return self.finished

	def isPaused(self):
		return self.paused

	def restart(self):
		self.__init__(self.startingProgram, self.inputType)

	def resume(self):
		self.calculate()

	def convertToDict(self):
		d={}
		for i in range(len(self.program)):
			d[i]=self.program[i]
		self.program=d



	def addInput(self, num):
		if self.inputType=="continuous":
			self.inputs.append(num)
		elif self.inputType=="raw":
			self.input=num

	def opCode(self, num):
		op=num%100
		result=[op]
		num=num//100
		for i in range(3):
			result.append(num%10)
			num=num//10

		return result

	def getParams(self, op, params):
		for p in range(len(params)):

			if op[p+1]==0:
				params[p]=self.program[params[p]]
			if op[p+1]==1:
				pass
			if op[p+1] == 2:
				
				params[p]=self.program[params[p]]+self.base
		return params


	def addMemory(self, num):
		self.program[num]=0

	def getOutput(self):
		return self.output


	def op1(self, op):
		a=self.pos+1
		b=self.pos+2
		res=self.pos+3
		params=self.getParams(op, [a, b, res])

		self.program[params[2]]=self.program[params[0]]+self.program[params[1]]
		self.pos+=4

	def op2(self, op):
		a=self.pos+1
		b=self.pos+2
		res=self.pos+3
		params=self.getParams(op, [a, b, res])
		self.program[params[2]]=self.program[params[0]]*self.program[params[1]]
		# print(self.program[params[2]])
		self.pos+=4

	def op3(self, op):
		a=self.pos+1
		params=self.getParams(op, [a])
		if self.inputType=="continuous":
			self.program[params[0]]=self.inputs[self.inputNum]
			self.inputNum+=1
		elif self.inputType=="raw":
			self.program[params[0]]=self.input
		elif self.inputType=="manual":
			self.program[params[0]]=int(input())
		self.pos+=2
		

	def op4(self, op):
		a=self.pos+1
		params=self.getParams(op, [a])
		output=self.program[params[0]]
		self.paused=True
		self.pos+=2
		self.output=output
		return output
		

	def op5(self, op):
		a=self.pos+1
		b=self.pos+2
		params=self.getParams(op, [a, b])
		if self.program[params[0]]!=0:
			self.pos=self.program[params[1]]
		else:
			self.pos+=3

	def op6(self, op):
		a=self.pos+1
		b=self.pos+2
		params=self.getParams(op, [a, b])
		if self.program[params[0]]==0:
			self.pos=self.program[params[1]]
		else:
			self.pos+=3
		

	def op7(self, op):
		a=self.pos+1
		b=self.pos+2
		res=self.pos+3
		params=self.getParams(op, [a, b, res])
		if self.program[params[0]]<self.program[params[1]]:
			self.program[params[2]]=1
		else:
			self.program[params[2]]=0
		self.pos+=4

	def op8(self, op):
		a=self.pos+1
		b=self.pos+2
		res=self.pos+3
		params=self.getParams(op, [a, b, res])
		if self.program[params[0]]==self.program[params[1]]:
			self.program[params[2]]=1
		else:
			self.program[params[2]]=0
		self.pos+=4

	def op9(self, op):
		a=self.pos+1
		params=self.getParams(op, [a])
		self.base+=self.program[params[0]]
		self.pos+=2



	def calculate(self):
		self.paused=False
		self.line=0
		while self.program[self.pos]!=99:
			try:
			# print(self.pos)
				self.line+=1
				op=self.opCode(self.program[self.pos])
				# print(op)
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

				elif op[0]==9:
					self.op9(op)

				else:

					print("error")
					print(op)
					break


			except KeyError as e:
				# print("dict error")
				self.addMemory(e.args[0])



		self.finished=True
		return self.output
