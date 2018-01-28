Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list(filter(None,0,1,False,True))
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    list(filter(None,0,1,False,True))
TypeError: filter expected 2 arguments, got 5
>>> list(filter(None,[0,1,False,True]))
[1, True]
>>> 
>>> 
>>> def odd(x):
	return x%2

>>> show = filter(odd,range(10))
>>> list(show)
[1, 3, 5, 7, 9]
>>> list(filter(lambda x:x%2,range(10)))
[1, 3, 5, 7, 9]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> odd(5)
1
>>> list(map(lambda x:x%2,range(10)))
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
>>> list(map(lambda x:x*2,range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> 
