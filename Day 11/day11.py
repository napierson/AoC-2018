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
		grid[(x, y)] = {1:power}

max_power = 0
max_x = 0
max_y = 0
max_n = 0


for n in range(2, 301):
	for x in range(1, 302 - n):
		for y in range(1, 302 - n):
			if n % 2 == 0:
				grid[(x, y)][n] = grid[(x, y)][n/2] + grid[(x + n/2, y)][n/2] +\
								grid[(x, y + n/2)][n/2] + grid[(x + n/2, y + n/2)][n/2]
			else:
				grid[(x, y)][n] = grid[(x, y)][n//2 + 1] + grid[(x + n//2 + 1, y)][n//2] +\
								grid[(x, y + n//2 + 1)][n//2] + grid[(x + n//2, y + n//2)][n//2 + 1] -\
								grid[(x + n//2, y + n//2)][1]
			if grid[(x, y)][n] > max_power:
				max_power = grid[(x, y)][n]
				max_x = x
				max_y = y
				max_n = n

print(max_x, max_y, max_n, grid[(max_x, max_y)][max_n], max_power)