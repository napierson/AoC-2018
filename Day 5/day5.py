with open("input.txt", "r") as f:
	polymer = f.read()

polymer = polymer.strip("\n")

lowers = "abdcefghijklmnopqrstuvwxyz"
uppers = lowers.upper()
pairs = []
for i in range(26):
	pairs.append("%c%c" % (lowers[i], uppers[i]))
	pairs.append("%c%c" % (uppers[i], lowers[i]))

print(pairs)

def unreacted(p):
	return any(pair in p for pair in pairs)

while unreacted(polymer):
	for i in range(len(polymer) - 1):
		if polymer[i:i+2] in pairs:
			polymer = polymer[:i] + polymer[i+2:]
			break

print(len(polymer))