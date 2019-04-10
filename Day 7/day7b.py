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
free_at = {x:0 for x in range(5)}
task_of = {x:None for x in free_at.keys()}

pending = set(adj.keys())
wip = set()
completed = set()

def available():
	return sorted([a for a in pending if not reverse[a]])

def idle():
	return sorted([m for m in task_of.keys() if task_of[m] == None])

def busy():
	return sorted([m for m in task_of.keys() if task_of[m] != None])

def advance_time():
	global time
	time = min([free_at[m] for m in busy()])
	for m in busy():
		if free_at[m] <= time:
			wip.remove(task_of[m])
			completed.add(task_of[m])
			#print("Machine %d completed task %s at time %d" % (m, task_of[m], free_at[m]))
			for v in adj[task_of[m]]:
				reverse[v].remove(task_of[m])
			task_of[m] = None

def assign():
	global time
	if available() and idle():
		todo = available()[0]
		m = idle()[0]
		task_of[m] = todo
		free_at[m] = time + dur[todo]
		pending.remove(todo)
		wip.add(todo)
	else:
		advance_time()

time = 0
while pending or wip:
	assign()

print(free_at)