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
nearest = {}
region_count = {}
for i in range(len(coords_tree.data)):
	region_count[str(coords_tree.data[i])] = 0

print(region_count)

for x in range(xmin, xmax + 1):
	for y in range(ymin, ymax + 1):
		pass
		#distances, pts = coords_tree.query([x, y], k = 2, p = 1)
		#if distances[0] < distances[1]:

