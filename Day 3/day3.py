with open("input.txt", "r") as f:
	claims = f.readlines()

for i in range(len(claims)):
	claims[i] = claims[i].split()
	del claims[i][1]
	claim_dict = {}
	claim_dict["id"] = int(claims[i][0].strip("#"))

	col, row = claims[i][1].strip(":").split(",")
	claim_dict["col_start"] = int(col)
	claim_dict["row_start"] = int(row)

	col, row = claims[i][2].split("x")
	claim_dict["col_end"] = claim_dict["col_start"] + int(col)
	claim_dict["row_end"] = claim_dict["row_start"]  + int(row)

	claims[i] = claim_dict

claimants = {}
for c in claims:
	for col in range(c["col_start"], c["col_end"]):
		for row in range(c["row_start"], c["row_end"]):
			loc = "%d, %d" % (col, row)
			if loc not in claimants.keys():
				claimants[loc] = 1
			else:
				claimants[loc] += 1

double_claimed = 0
for count in claimants.values():
	if count >= 2:
		double_claimed += 1

print(double_claimed)

def uncontested(id):
	for col in range(claims[id]["col_start"], claims[id]["col_end"]):
		for row in range(claims[id]["row_start"], claims[id]["row_end"]):
			loc = "%d, %d" % (col, row)
			if claimants[loc] >= 2:
				return False

	return True

for c in claims:
	if uncontested(c["id"] - 1):
		print(c["id"])