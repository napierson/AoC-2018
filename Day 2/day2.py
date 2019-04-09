with open("input.txt", "r") as f:
	box_IDs = f.readlines()

for i in range(len(box_IDs)):
	box_IDs[i] = box_IDs[i].strip()

def counts(id):
	counts = {}
	for letter in id:
		if letter not in counts.keys():
			counts[letter] = 1
		else:
			counts[letter] += 1
	return counts

twos = 0
threes = 0
for id in box_IDs:
	c = counts(id)
	if 2 in c.values():
		twos += 1
	if 3 in c.values():
		threes += 1

print(twos)
print(threes)
print(twos * threes)

def diff_count(x, y):
	d = 0
	for i in range(len(x)):
		if x[i] != y[i]:
			d += 1
	return d

for x in box_IDs:
	for y in box_IDs:
		if diff_count(x, y) == 1:
			print(x)
			print(y)