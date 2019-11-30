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
