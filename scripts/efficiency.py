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

def memo(f):
	"""Creates a cache for storing 
	all the calculated arguments before
	for instance: we want to calculate how many times the 
	fib function is called during the use of memo version.
	在多层嵌套结构中，实际上只要保证递归函数调用最上层函数即可。
	例如在这里fib 会调用memoized， memoized 会调用count_version
	count_version 则继续调用f f又调用fib。
	>>> fib = count(fib)
	>>> fib = memo(fib)
	"""
	cache = {}
	def memoized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized
