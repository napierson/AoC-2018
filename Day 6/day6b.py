with open("input.txt", "r") as f:
	coords = f.readlines()

for i in range(len(coords)):
	coords[i] = coords[i].strip("\n").split(",")
	coords[i] = [int(coords[i][0]), int(coords[i][1])]

print(len(coords))

xcoords = sorted(coords, key = lambda c: c[0])
xmin = xcoords[0][0]
xmax = xcoords[-1][0]

ycoords = sorted(coords, key = lambda c: c[1])
ymin = ycoords[0][1]
ymax = ycoords[-1][1]

print(xmin, xmax, ymin, ymax)


def total_dist(pt):
	return sum(abs(pt[0] - c[0]) + abs(pt[1] - c[1]) for c in coords)

safe_ct = 0
for x in range(xmin, xmax + 1):
	for y in range(ymin, ymax + 1):
		if total_dist([x, y]) < 10000:
			safe_ct += 1

print(safe_ct)