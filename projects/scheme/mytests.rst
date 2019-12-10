This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

    >>> from scheme_reader import *

    Case Example
        >>> scheme_read(Buffer(tokenize_lines(['nil'])))
        nil

    Case read_tail:
    	>>> test = Buffer(tokenize_lines(['(1 2)']))
    	>>> test.remove_front()
    	'('
    	>>> scheme_read(test)
    	1
    	>>> test.current()
    	2
    	>>> scheme_read(test)
    	2
    	>>> test.current()
    	')'
    	>>> read_tail(test)
    	nil
    	>>> test.current()

Suite 2:

	>>> from scheme_reader import *
	>>> from scheme import *

    Case Question5:
    	>>> expr = read_line('(+ 2 2)')
    	>>> print(expr.first)
    	+
    	>>> expr.first
    	'+'
    	>>> expr.second
    	Pair(2, Pair(2, nil))

    Case Q52:
    	>>> expr = read_line('(+ (+ 1 2) (* 1 4))')
    	>>> expr
    	Pair('+', Pair(Pair('+', Pair(1, Pair(2, nil))), Pair(Pair('*', Pair(1, Pair(4, nil))), nil)))





