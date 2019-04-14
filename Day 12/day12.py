with open("input.txt", "r") as f:
	init_state = f.readlines()

rules = init_state[2:]
for i in range(len(rules)):
	rules[i] = rules[i].strip("\n").split(" => ")
rules = {rules[i][0]:rules[i][1] for i in range(len(rules))}

init_state[0] = init_state[0].strip("initial state: ").strip("\n")

#invariant: the leftmost pot in pots.keys() is #
pots = {i:init_state[0][i] for i in range(len(init_state[0]))}

def advance_gen():
	global pots
	next_gen = {}
	left = min(pots.keys()) - 1
	next_gen[left] = rules["".join(["...", pots[left + 1], pots[left + 2]])]

	left += 1
	next_gen[left] = rules["".join(["..", pots[left], pots[left + 1], pots[left + 2]])]

	left += 1
	next_gen[left] = rules["".join([".", pots[left - 1], pots[left], pots[left + 1], pots[left + 2]])]

	for i in range(left + 1, max(pots.keys()) - 1):
		next_gen[i] = rules["".join([pots[j] for j in range(i - 2, i + 3)])]

	right = max(pots.keys()) - 1
	next_gen[right] = rules["".join([pots[right - 2], pots[right - 1], pots[right], pots[right + 1], "."])]

	right += 1
	next_gen[right] = rules["".join([pots[right - 2], pots[right - 1], pots[right], ".."])]

	right += 1
	next_gen[right] = rules["".join([pots[right - 2], pots[right - 1], "..."])]

	ngmin = min(next_gen.keys())
	ngmax = max(next_gen.keys())
	to_del = []
	while next_gen[ngmin] == ".":
		to_del.append(ngmin)
		ngmin += 1

	while next_gen[ngmax] == ".":
		to_del.append(ngmax)
		ngmax -= 1

	for i in to_del:
		del next_gen[i]
	
	pots = next_gen

gens = 20000
for i in range(gens):
	advance_gen()

print(50*gens + 695)

checksum = sum([p for p in pots.keys() if pots[p] == "#"])
print(checksum)

print(50*50000000000 + 695)