class Link:
	"""The Linked List implemented by using Recursive objects
    >>> s = Link(3, Link(4, Link(7)))
    >>> s[2]
    7
    >>> len(s)
    3
    >>> s
    Link(3, Link(4, Link(7)))
    >>> s = Link(3, Link(4, Link(7, Link(10))))
    >>> s
    Link(3, Link(4, Link(7, Link(10))))
    >>> s_new = Link(s, Link(7))
    >>> s_new
    Link(Link(3, Link(4, Link(7, Link(10)))), Link(7))
    >>> s + s
    Link(3, Link(4, Link(7, Link(10, Link(3, Link(4, Link(7, Link(10))))))))
	"""
	empty = ()
	def __init__(self, first, rest = empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i-1]

	def __len__(self):
		return 1 + len(self.rest)

	def __repr__(self):
		if self.rest is Link.empty:
			rest = ''
			return 'Link({0})'.format(self.first)
		rest = self.rest.__repr__()
		return 'Link({0}, {1})'.format(self.first, rest)

	def __add__(self, new_link):
		"""The add function should create a new object instead of 
		altering the current object."""
		if self.rest is Link.empty:
			return Link(self.first, new_link)
		else:
			return Link(self.first, self.rest.__add__(new_link))


def map_link(f, s):
	"""Apply f to each element of a Linked List
	>>> s = Link(2, Link(4, Link(8)))
	>>> square = lambda x: x*x
	>>> map_link(square, s)
	Link(4, Link(16, Link(64)))
	"""
	if s is Link.empty:
		return s
	else:
		return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
	"""Return a new Linked List for which a function f returns true
	>>> odd = lambda x: x % 2 == 1
	>>> s = Link(1, Link(5, Link(8, Link(3, Link(10)))))
	>>> filter_link(odd, s)
	Link(1, Link(5, Link(3)))
	"""
	if s is Link.empty:
		return s
	else:
		if f(s.first):
			return Link(s.first, filter_link(f, s.rest))
		else:
			return filter_link(f, s.rest)


def join_link(s, separator):
	"""
    >>> s = Link(3, Link(4, Link(5)))
    >>> join_link(s, ", ")
    '3, 4, 5'
	"""
	if s is Link.empty:
		return ''
	elif s.rest is Link.empty:
		return str(s.first)
	else:
		return str(s.first) + separator + join_link(s.rest, separator)


def partitions(n, m):
	"""Return a Linked List containing a list of Lists.
	 """
	if n == 0:
		return Link(Link.empty)
	elif n < 0 or m == 0:
		return Link(Link.empty)
	else:
		using_m = partitions(n-m, m)
		with_m = map_link(lambda s: Link(m, s), using_m)
		without_m = partitions(n, m-1)
		return with_m + without_m

def print_partitions(n, m):
	lists = partitions(n, m)
	strings = map_link(lambda s:join_link(s, " + "), lists)
	print(join_link(strings, "\n"))


class Tree:

	
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



def empty(s):
	return s is Link.empty


def set_contains(s, v):
	"""Return true if set s contains v
	>>> s = Link(4, Link(1, Link(5)))
	>>> set_contains(s, 1)
	True
	>>> set_contains(s, 10)
	False
	"""
	if empty(s):
		return False
	elif s.first == v:
		return True
	else:
		return set_contains(s.rest, v)



def adjoin_set(s, v):
	if set_contains(s, v):
		return s
	else:
		return Link(v, s)


def intersect_set(set1, set2):
	"""
	>>> set1 = Link(1, Link(3, Link(5, Link(8))))
	>>> set2 = Link(2, Link(3, Link(7, Link(8))))
	>>> intersect_set(set1, set2)
	Link(3, Link(8))
	"""
	if empty(set1) or empty(set2):
		return Link.empty
	else:
		e1, e2 = set1.first, set2.first
		if e1 == e2:
			return Link(e1, intersect_set(set1.rest, set2))
		elif e1 < e2:
			return intersect_set(set1.rest, set2)
		elif e2 < e1:
			return intersect_set(set1, set2.rest)








