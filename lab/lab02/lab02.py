"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions
#
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add) # Return a new function
    >>> add_three = curried_add(3)       # Return another new function.
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: func(x, y)
