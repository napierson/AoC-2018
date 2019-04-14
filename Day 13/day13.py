with open("input.txt", "r") as f:
	tracks = f.readlines()

print(list(tracks[0][-10:]))