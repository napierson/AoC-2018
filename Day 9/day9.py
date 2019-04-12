with open("input.txt", "r") as f:
	data = f.read()
	data = data.split()
	player_ct = int(data[0])
	marble_max = int(data[6])

marbles = [0]
# value of the next marble to add
next_marble = 1
# index of the current marble
cur_marble = 0
cur_player = 0
scores = {p:0 for p in range(player_ct)}

def play_marble():
	global next_marble, marbles, cur_marble, cur_player, player_ct
	#print("Initial:", cur_marble, marbles[cur_marble], marbles)
	if next_marble % 23 != 0:
		insert_at = ((cur_marble + 1) % len(marbles)) + 1
		marbles.insert(insert_at, next_marble)
		#print("After insertion:", cur_marble, marbles[cur_marble], marbles)
		cur_marble = insert_at
		#print("New current marble:", cur_marble, marbles[cur_marble], marbles)
	else:
		scores[cur_player] += next_marble
		cur_marble = (cur_marble - 7) % len(marbles)
		scores[cur_player] += marbles.pop(cur_marble)
	cur_player = (cur_player + 1) % player_ct
	next_marble += 1

for i in range(marble_max):
	play_marble()

print(max(scores.values()))