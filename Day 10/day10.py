with open("input.txt", "r") as f:
	stars = f.readlines()

for i in range(len(stars)):
	star = stars[i].strip("position=<").split()
	star[0] = star[0].strip(",")
	star[1] = star[1].strip(">")
	star[2] = star[2].strip("velocity=<")
	if not star[2]:
		del star[2]
	star[2] = star[2].strip(",")
	star[3] = star[3].strip(">")
	stars[i] = {"px": int(star[0]), "py": int(star[1]), "vx": int(star[2]), "vy": int(star[3])}

def advance(t):
	for star in stars:
		star["px"] += t * star["vx"]
		star["py"] += t * star["vy"]

advance(10407)
xmax = max([star["px"] for star in stars])
xmin =  min([star["px"] for star in stars])
ymax =  max([star["py"] for star in stars])
ymin =  min([star["py"] for star in stars])

msg_grid = {"%d, %d" % (star["px"], star["py"]): "#" for star in stars}

for y in range(ymin, ymax + 1):
	line = ""
	for x in range(xmin, xmax + 1):
		if "%d, %d" % (x, y) in msg_grid.keys():
			line = line + "#"
		else:
			line = line + "."
	print(line)