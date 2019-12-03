def calculate(num):
	return (num//3)-2

def recursiveFuel(num):
	fuelneeded=calculate(num)
	if fuelneeded<=0:
		return 0
	return fuelneeded+recursiveFuel(fuelneeded)

print (recursiveFuel(100756))

with open("input.txt", "r") as f:
	total=0
	total2=0
	for line in f:
		num=int(line.strip())
		total+=calculate(num)
		total2+=recursiveFuel(num)
	print(total)
	print(total2)