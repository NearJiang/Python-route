Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def U(x):
	return 2*x+1

>>> U(5)
11
>>> lambda x : 2*x+1
<function <lambda> at 0x02893300>
>>> lambada 2
SyntaxError: invalid syntax
>>> lambda2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    lambda2
NameError: name 'lambda2' is not defined
>>> lambda '2'
SyntaxError: invalid syntax
>>> g = lambda x :2*x+1
>>> g(5)
11
>>> 
>>> 
>>> def add(x,y):
	return x+y

>>> add(3+6)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    add(3+6)
TypeError: add() missing 1 required positional argument: 'y'
>>> add(3,6)
9
>>> lambda x,y:x+y
<function <lambda> at 0x0314CFA8>
>>> g=lambda x,y:x+y
>>> g(5,6)
11
>>> 
