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


print(adj, "\n")
print(reverse, "\n")

visited = set()
verts = []

def topsort(v):
	visited.add(v)
	for w in adj[v]:
		if w not in visited:
			topsort(w)
	verts.append(v)

for v in adj.keys():
	if v not in visited:
		topsort(v)

visited = set()
def available():
	return sorted([a for a in reverse.keys() if (not reverse[a] and a not in visited)])

def execute():
	todo = available()[0]
	visited.add(todo)
	for v in adj[todo]:
		reverse[v].remove(todo)
	return todo

steps = []
while available():
	steps.append(execute())

print("".join(steps))