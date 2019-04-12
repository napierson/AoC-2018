serial = 8772
grid = {}
for x in range(1, 301):
	for y in range(1, 301):
		rack_id = x + 10
		power = rack_id * y
		power += serial
		power *= rack_id
		power = str(power)
		if len(power) >= 3:
			power = int(power[-3])
		else:
			power = 0
		power -= 5
		grid["%d,%d" % (x, y)] = [power]

def square_power(x, y, n):
	power = 0
	for i in range(x, x+n):
		for j in range(y, y+n):
			power += grid["%d,%d" % (i, j)]

	return power

max_power = 0
max_x = 1
max_y = 1
max_n = 1

for x in range(1, 300):
	for y in range(1, 300):
		for n in range(2, min([25, 301 - x, 301 - y])):
			next_power = grid["%d,%d" % (x, y)][-1]
			for i in range(n):
				next_power += grid["%d,%d" % (x + n, y + i)][0]
				next_power += grid["%d,%d" % (x + i, y + n)][0]
			next_power += grid["%d,%d" % (x + n, y + n)][0]
			grid["%d,%d" % (x, y)].append(next_power)

for x in range(1, 301):
	for y in range(1, 301):
		cur_power = max(grid["%d,%d" % (x, y)])
		cur_n = grid["%d,%d" % (x, y)].index(cur_power) + 1
		if cur_power > max_power:
			max_power = cur_power
			max_x = x
			max_y = y
			max_n = cur_n

print(max_x, max_y, max_n)