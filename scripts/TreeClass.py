class Tree:

	"""
	>>> Tree(3, (Tree(1, (Tree(0), Tree(1))), Tree(2, (Tree(1), Tree(1, (Tree(0), Tree(1)))))))"""
	def __init__(self, label, branches=()):
		self.label = label
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = branches

	def __repr__(self):
		if self.branches:
			#Guess the only explantation is that the __repr__ method in tuple 
			#will invoke the __repr__ method for every elements inside.
			return 'Tree({0}, {1})'.format(self.label, self.branches.__repr__())
		else:
			return 'Tree({0})'.format(self.label)

	def is_leaf(self):
		return not self.branches	



def fib_tree(n):
	if n == 0 or n == 1:
		return Tree(n)
	else:
		left = fib_tree(n - 2)
		right = fib_tree(n - 1)
		return Tree(left.label + right.label, (left, right))


def sum_labels(t):
	 return t.label + sum([sum_labels(b) for b in t.branches])