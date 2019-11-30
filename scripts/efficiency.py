def fib(n):
	"""Return the n th term of a fibnacci series.
	>>> fib(0)
	0
	>>> fib(5)
	5
	"""
	if n == 0 or n == 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)


def count(f):
	"""Decleared as a decorator that holds the information
	about how many times a function are called.
	Only in this way can this fits for fib:
	fib = count(f)
	"""
	def counted(*args):
		counted.call_count += 1
		return f(*args)

	counted.call_count = 0
	return counted

def count_frames(f):
	"""Count the maximum active frames during the execution."""
	def counted(*args):
		counted.open_count += 1
		if counted.open_count > counted.max_count:
			counted.max_count = counted.open_count
		result = f(*args)
		counted.open_count -= 1
		return result
	counted.open_count = 0
	counted.max_count = 0
	return counted

