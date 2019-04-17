with open("input.txt", "r") as f:
	tracks_raw = f.readlines()

class Cart:
	# Coordinate offsets for north, east, south, west
	# 0: north, 1: east, 2: south, 3: west
	DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

	# Offsets for a turn. If you're currently facing DIRS[i],
	# then DIRS[i - 1] will be a left turn, DIRS[i + 1] will be
	# a right turn, and DIRS[i + 0] is continuing straight ahead.
	TURNS = {"L":-1, "S":0, "R":1}

	def __init__(self, x, y, d):
		self.px = x
		self.py = y
		self.facing = d
		self.next_turn = "L"

	def turn(self, t):
		self.facing = (self.facing + Cart.TURNS[t]) % len(Cart.DIRS)

	def advance(self):
		cur_track = tracks[(self.px, self.py)]
		if cur_track == "/":
			if self.facing == 0 or self.facing == 2:
				self.turn("R")
			else:
				self.turn("L")
		elif cur_track == "\\":
			if self.facing == 0 or self.facing == 2:
				self.turn("L")
			else:
				self.turn("R")
		elif cur_track == "+":
			self.turn(self.next_turn)
			if self.next_turn == "L":
				self.next_turn == "S"
			elif self.next_turn == "S":
				self.next_turn == "R"
			else:
				self.next_turn == "L"

		self.px += Cart.DIRS[self.facing][0]
		self.py += Cart.DIRS[self.facing][1]

		return self.px, self.py

cart_pos = set()
carts = []
tracks = {}

for y in range(len(tracks_raw)):
	tracks_raw[y] = list(tracks_raw[y])
	for x in range(len(tracks_raw[y])):
		if tracks_raw[y][x] in "/|-+\\":
			tracks[(x, y)] = tracks_raw[y][x]
		elif tracks_raw[y][x] == "^":
			tracks[(x, y)] = "|"
			carts.append(Cart(x, y, 0))
			cart_pos.add((x, y))
		elif tracks_raw[y][x] == "v":
			tracks[(x, y)] = "|"
			carts.append(Cart(x, y, 2))
			cart_pos.add((x, y))
		elif tracks_raw[y][x] == ">":
			tracks[(x, y)] = "-"
			carts.append(Cart(x, y, 1))
			cart_pos.add((x, y))
		elif tracks_raw[y][x] == "<":
			tracks[(x, y)] = "-"
			carts.append(Cart(x, y, 3))
			cart_pos.add((x, y))

tick_ct = 0
def tick():
	global tick_ct
	tick_ct += 1
	for c in sorted(carts, key = lambda c:(c.py, c.px)):
		#print("Cart at: (%d, %d)" % (c.px, c.py))
		cart_pos.remove((c.px, c.py))
		new_pos = c.advance()
		#print("Moved to: (%d, %d)\n" % new_pos)
		if new_pos in cart_pos:
			return new_pos
		else:
			cart_pos.add(new_pos)

	return None

collision = None
while not collision:
	collision = tick()

print(collision)
print(tick_ct)