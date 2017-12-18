alst=783
blst=325
# alst=65
# blst=8921

afactor=16807
bfactor=48271
mod=2147483647
judge=0

for i in range(5000000):

	alst=(alst*afactor)%mod
	while alst%4!=0:
		alst=(alst*afactor)%mod

	blst=(blst*bfactor)%mod
	while(blst%8!=0):
		blst=(blst*bfactor)%mod
	# print alst, blst
	if ("{:0>16}".format(bin(alst)[-16:])== "{:0>16}".format(bin(blst)[-16:])):
		judge+=1
print judge
