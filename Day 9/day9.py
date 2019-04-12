with open("input.txt", "r") as f:
	data = f.read()
	data = data.split()
	player_ct = int(data[0])
	marble_max = 100 * int(data[6])


class Marble:
	def __init__(self, value):
		self.next = self
		self.prev = self
		self.value = value

	def insert(self, m):
		m.next = self.next
		m.prev = self
		m.next.prev = m
		self.next = m

	def remove(self):
		self.prev.next = self.next
		self.next.prev = self.prev
		return self.next

cur_marble = Marble(0)
next_marble = 1
cur_player = 0
scores = {p:0 for p in range(player_ct)}

for i in range(marble_max):
	if next_marble % 23 != 0:
		cur_marble = cur_marble.next
		cur_marble.insert(Marble(next_marble))
		cur_marble = cur_marble.next
	else:
		scores[cur_player] += next_marble
		for j in range(7):
			cur_marble = cur_marble.prev
		scores[cur_player] += cur_marble.value
		cur_marble = cur_marble.remove()

	cur_player = (cur_player + 1) % player_ct
	next_marble += 1

print(max(scores.values()))