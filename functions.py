# 1. 
def area_t(a,b):
    ''' 
    returnes the divison of sum of a and b
    parametrs are: 
    	    a - is int or float
            b - is int or float
    '''
 #    c = (a + b)//2
	# return c
help(area_t)
print(area_t.__doc__)
# # 2.
def str_(a):
	'''
	name: slice statement
	meaning: returnes reversed version of the given string
	parametrs are: the biggining of the string, -1
	returnes: start at string length, end at position 0, move with the step -1
	'''
	rev_str = a[::-1]
	return rev_str
help(str_)
print(str_.__doc__)
# # 3.
# 	# def isupper():
# 	# 	c = i.isupper()
# 	# 	return c
# 	# def islower():
# 	# 	d = i.islower()
# 	# 	return d