with open("input.txt", "r") as f:
	sleep_logs = f.readlines()

for i in range(len(sleep_logs)):
	sleep_logs[i] = sleep_logs[i].strip("\n").split("]")
	sleep_logs[i][0] = sleep_logs[i][0].strip("[")
	sleep_logs[i][1] = sleep_logs[i][1].strip(" ")
	if "#" in sleep_logs[i][1]:
		sleep_logs[i][1] = int(sleep_logs[i][1].split(" ")[1].strip("#"))

	sleep_logs[i].append(int(sleep_logs[i][0].split(":")[1]))

sleep_logs = sorted(sleep_logs, key = lambda l: l[0])

sleep_recs = []
total_sleep = {}
g_id = 0
for l_id in range(len(sleep_logs)):
	if isinstance(sleep_logs[l_id][1], int):
		g_id = sleep_logs[l_id][1]
		if g_id not in total_sleep.keys():
			total_sleep[g_id] = 0
	elif sleep_logs[l_id][1] == "wakes up":
		total_sleep[g_id] += sleep_logs[l_id][2] - sleep_logs[l_id - 1][2]
		sleep_recs.append([g_id, sleep_logs[l_id - 1][2], sleep_logs[l_id][2], sleep_logs[l_id][2] - sleep_logs[l_id - 1][2]])

print(total_sleep)

sleepiest = 0
slept_for = 0
for g_id in total_sleep.keys():
	if total_sleep[g_id] > slept_for:
		sleepiest = g_id
		slept_for = total_sleep[g_id]

print(sleepiest)
print(slept_for)

sleepiest_recs = [rec for rec in sleep_recs if rec[0] == sleepiest]

times_slept = {}
for i in range(60):
	times_slept[i] = 0

for rec in sleepiest_recs:
	for t in range(rec[1], rec[2]):
		times_slept[t] += 1

best_time = 0
sc = times_slept[0]
for t, v in times_slept.items():
	if v > sc:
		best_time = t
		sc = v

print(best_time)
print(sleepiest * best_time)

sleep_counts = {}
for g_id in total_sleep.keys():
	sleep_counts[g_id] = {}
	for t in range(60):
		sleep_counts[g_id][t] = 0

for rec in sleep_recs:
	for t in range(rec[1], rec[2]):
		sleep_counts[rec[0]][t] += 1

best_g = 0
best_m = 0
gm_ct = 0
for g_id in sleep_counts.keys():
	for m in sleep_counts[g_id].keys():
		if sleep_counts[g_id][m] > gm_ct:
			best_g = g_id
			best_m = m
			gm_ct = sleep_counts[g_id][m]

print(best_g)
print(best_m)
print(best_g * best_m)