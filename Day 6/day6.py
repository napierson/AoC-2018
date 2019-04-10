with open("input.txt", "r") as f:
	coords = f.readlines()

for i in range(len(coords)):
	coords[i] = coords[i].strip("\n").split(",")
	coords[i] = {'x': int(coords[i][0]), 'y': int(coords[i][1])}

print(coords[:10])