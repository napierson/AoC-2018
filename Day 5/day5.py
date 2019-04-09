import re

with open("input.txt", "r") as f:
	polymer = f.read()

polymer = polymer.strip("\n")

lowers = "abdcefghijklmnopqrstuvwxyz"
uppers = lowers.upper()
pairs = []
for i in range(26):
	pairs.append("%c%c" % (lowers[i], uppers[i]))
	pairs.append("%c%c" % (uppers[i], lowers[i]))

print(pairs)

def opposite_polarity(a, b):
	return a != b and (a.upper() == b or a.lower() == b)

print(opposite_polarity('b', 'A'))

def react(p):
	p_stack = []
	for u in p:
		if not p_stack or not opposite_polarity(p_stack[-1], u):
			p_stack.append(u)
		else:
			p_stack.pop()
	return "".join(p_stack)

test = "abcDEFabc"
test = re.sub('[ac]', '', test)
print(test)

reacted = react(polymer)
print(len(reacted))
shortest = len(reacted)
for i in range(26):
	reduced = re.sub('[%c%c]' % (lowers[i], uppers[i]), '', reacted)
	reduced = react(reduced)
	if len(reduced) < shortest:
		shortest = len(reduced)

print(shortest)