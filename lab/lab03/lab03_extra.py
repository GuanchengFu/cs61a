""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def func_return(n):
        if n == 0:
            return lambda x: x
        if n % 3 == 1:
            return lambda y: f1(func_return(n - 1)(y))
        elif n % 3 == 2:
            return lambda x: f2(func_return(n - 1)(x))
        elif n % 3 == 0:
            return lambda x: f3(func_return(n - 1)(x))
    return func_return


## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: 10*y + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def inside(m):
        if m == 1:
            return True
        if n % m == 0:
            return False
        else:
            return inside(m - 1)
    return inside(n - 1)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def inside(m, flag):
        if m == n:
            if flag:
                return odd_term(n)
            else:
                return even_term(n)
        else:
            if flag:
                flag = not flag
                return odd_term(m) + inside(m + 1, flag)
            else:
                flag = not flag
                return even_term(m) + inside(m + 1, flag)
    if n == 1:
        return odd_term(1)
    else:
        return odd_term(1) + inside(2, False)



def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def digit(m, n):
        if n != 0:
            if n % 10 == m:
                return 1 + digit(m, n // 10)
            else:
                return digit(m, n // 10)
        else:
            return 0
    if digit(5, n) == 1:
        return int(digit(1, n) * digit(9, n) + digit(2, n) * digit(8, n) + digit(3, n) * digit(7, n) + digit(4, n) * digit(
            6, n))
    else:
        return int(digit(1, n) * digit(9, n) + digit(2, n) * digit(8, n) + digit(3, n) * digit(7, n) + digit(4, n) * digit(6, n) + (1 + digit(5, n) - 1) * (digit(5, n) - 1) / 2)
