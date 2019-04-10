with open("input.txt", "r") as f:
	prereqs = f.readlines()

adj = {}
reverse = {}
for p in prereqs:
	steps = p.split()
	before, after = steps[1], steps[7]
	if after not in adj.keys():
		adj[after] = []
	if before not in adj.keys():
		adj[before] = [after]
	else:
		adj[before].append(after)

	if before not in reverse.keys():
		reverse[before] = []
	if after not in reverse.keys():
		reverse[after] = [before]
	else:
		reverse[after].append(before)