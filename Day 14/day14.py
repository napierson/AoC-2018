num_recipes = 323081

recipes = [3, 7]
pa = 0
pb = 1

def add_recipes():
	global recipes, pa, pb
	score = recipes[pa] + recipes[pb]
	score = [int(s) for s in list(str(score))]
	for s in score:
		recipes.append(s)

	pa = (pa + 1 + recipes[pa]) % len(recipes)
	pb = (pb + 1 + recipes[pb]) % len(recipes)

for i in range(5):
	add_recipes()

def has_key():
	global recipes
	target = str(num_recipes)
	to_check = recipes[-len(target)-1:]
	to_check = "".join([str(i) for i in to_check])
	return target in to_check

while not has_key():
	add_recipes()

print(len(recipes))
print(recipes[-len(str(num_recipes))-1:])