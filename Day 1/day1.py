with open("input.txt") as f:
	freq_deltas = f.readlines()

for i in range(0, len(freq_deltas)):
	freq_deltas[i] = int(freq_deltas[i].strip("+\n"))

freq = 0
for delta in freq_deltas:
	freq += delta

print(freq)

freq = 0
idx = 0
freqs_reached = set()
while freq not in freqs_reached:
	freqs_reached.add(freq)
	freq += freq_deltas[idx]
	idx = (idx + 1) % len(freq_deltas)

print(freq)