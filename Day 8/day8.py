with open("input.txt", "r") as f:
	license = f.read()

license = license.split()
for i in range(len(license)):
	license[i] = int(license[i])

class Node:
	def __init__(self):
		self.child_ct = 0
		self.metadata_ct = 0
		self.children = []
		self.metadata = []

	def metasum(self):
		return sum(self.metadata) + sum([c.metasum() for c in self.children])

	def makenode(ptr):
		global license
		newnode = Node()
		newnode.child_ct = license[ptr]
		ptr += 1
		newnode.metadata_ct = license[ptr]
		ptr += 1
		for i in range(newnode.child_ct):
			ptr, child = Node.makenode(ptr)
			newnode.children.append(child)
		for i in range(newnode.metadata_ct):
			newnode.metadata.append(license[ptr])
			ptr += 1

		return ptr, newnode

	def value(self):
		if self.child_ct == 0:
			return sum(self.metadata)
		else:
			v = 0
			for m in self.metadata:
				if m <= self.child_ct:
					v += self.children[m - 1].value()
		return v

i, root = Node.makenode(0)
print(i)
print(root.child_ct)
print(root.metadata)
print(root.metasum())
print(root.value())