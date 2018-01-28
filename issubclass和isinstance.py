Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class a:
	pass

>>> class b:
	pass

>>> class b(a)
SyntaxError: invalid syntax
>>> class b(a):
	pass

>>> issubclass(b,a)
True
>>> issubclass(b,b)
True
>>> b1=b()
>>> isinstance(b1,b)
True
>>> isinstance(b1,a)
True
>>> isinstance(b1,(a,b))
True
>>> class c:
	pass

>>> 
>>> isinstance(b1,(a,b,c))
True
>>> 
