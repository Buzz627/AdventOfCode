
test=[[5, 9, 2, 8],
[9, 4, 7, 3],
[3, 8, 6, 5]]
with open("input.txt", "r") as f:
	star1=0
	star2=0
	for line in f:
		nums=map(lambda x:int(x), line.split())
		star1+=(max(nums)-min(nums))
		for i in nums:
			for j in nums:
				if i%j==0 and i!=j:
					star2+=i/j
	print star1
	print star2