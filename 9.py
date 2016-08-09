import test2
def fun():
	"""
	>>> for symbol in dir(test2):
	...	attr = getattr(test2, symbol)
	...	if (callable(attr) and attr.__name__.startswith('test_')):
	...		attr()
	True
	True
	True
	True
	True
	"""
	return 
if __name__=='__main__':
	import doctest
	doctest.testmod()
    	

