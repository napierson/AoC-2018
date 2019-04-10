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

dur = {x:ord(x) - 4 for x in adj.keys()}
free_at = {x:0 for x in [0, 1, 2, 3, 4]}

assigned = set()
completed = set()
def available():
	return sorted([a for a in reverse.keys() if (not reverse[a] and a not in assigned)])

time = 0
def assign():
	if available():
		todo = available()[0]
		for worker, avail in free_at.values():
			if avail <= time:
				free_at[worker] = time + dur[todo]
				assigned.add(todo)
				break