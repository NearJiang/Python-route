Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mix = ['a','b','c','d']
>>> mix.remove('c')
>>> 
>>> mix
['a', 'b', 'd']
>>> del mix[0]
>>> mix
['b', 'd']
>>> mix.pop()
'd'
>>> mix
['b']
>>> mix.append('222')
>>> mix
['b', '222']
>>> mix.pop(0)
'b'
>>> mix
['222']
>>> 
