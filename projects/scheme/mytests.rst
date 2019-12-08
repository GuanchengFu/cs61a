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


