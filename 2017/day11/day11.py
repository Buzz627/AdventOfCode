
commands={"n":0,"s":0,"nw":0,"ne":0,"sw":0,"se":0}
test="se,sw,se,sw,sw,sw,n"
with open ("input.txt", "r") as f:
	for line in f:
		lst=test.split(",")
		for i in lst:
			if i not in commands:
				commands[i]=0
			commands[i]+=1

total=0
north=commands["n"]-commands["s"]
# north=((commands["n"]+abs(commands["ne"]-commands["nw"]))-(commands["s"]+abs(commands["se"]-commands["sw"])))
northeast=(commands["ne"]-commands["sw"])
northwest=(commands["nw"]-commands["se"])
print north, northeast,northwest

print commands
commands["s"]+=min(commands["sw"], commands["se"])

commands["n"]+=min(commands["nw"], commands["ne"])
side=(commands["sw"]+commands["nw"])-(commands["se"]+commands["ne"])

print commands


# side=(max(northwest, northeast)-min(northwest, northeast))
# print side
# north+=side
# print north, max(northwest, northeast)-side

# print max(north, northwest, northeast)-min(north, northwest, northeast)

