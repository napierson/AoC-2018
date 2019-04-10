from scipy import spatial

with open("input.txt", "r") as f:
	coords = f.readlines()

for i in range(len(coords)):
	coords[i] = coords[i].strip("\n").split(",")
	coords[i] = [int(coords[i][0]), int(coords[i][1])]

xcoords = sorted(coords, key = lambda c: c[0])
xmin = xcoords[0][0]
xmax = xcoords[-1][0]

ycoords = sorted(coords, key = lambda c: c[1])
ymin = ycoords[0][1]
ymax = ycoords[-1][1]

print(xmin, xmax, ymin, ymax)

coords_tree = spatial.KDTree(coords)
parent_of = {}
region_ct = {}
for i in range(len(coords_tree.data)):
	region_ct[i] = 0

for x in range(xmin, xmax + 1):
	for y in range(ymin, ymax + 1):
		distances, pts = coords_tree.query([x, y], k = 2, p = 1)
		if distances[0] < distances[1]:
			region_ct[pts[0]] += 1
			parent_of["(%d, %d)" % (x, y)] = pts[0]
		else:
			parent_of["(%d, %d)" % (x, y)] = None

def above(pt):
	return any([c[1] - pt[1] > abs(c[0] - pt[0]) for c in ycoords[::-1]])

def left(pt):
	return any([pt[0] - c[0] > abs(c[1] - pt[1]) for c in xcoords])

def below(pt):
	return any([pt[1] - c[1] > abs(c[0] - pt[0]) for c in ycoords])

def right(pt):
	return any([c[0] - pt[0] > abs(c[1] - pt[1]) for c in xcoords[::-1]])

def covered(pt):
	return above(pt) and left(pt) and below(pt) and right(pt)

for k in sorted(region_ct.keys(), key = lambda k: -region_ct[k]):
	if covered(coords_tree.data[k]):
		print(coords_tree.data[k])
		print(region_ct[k])
		break