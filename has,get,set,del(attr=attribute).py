Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class A:
	def __init__(self,x=0):
		self.x=x

		
>>> a=A()
>>> hasattr(a,A)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    hasattr(a,A)
TypeError: hasattr(): attribute name must be string
>>> hasattr(a,x)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hasattr(a,x)
NameError: name 'x' is not defined
>>> hasattr(a,'x')
True
>>> getattr(a,'x')
0
>>> getattr(a,'y')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    getattr(a,'y')
AttributeError: 'A' object has no attribute 'y'
>>> getattr(a,'y','你所访问的属性不在地球人的认知中，骚年，去征服星辰大海吧')
'你所访问的属性不在地球人的认知中，骚年，去征服星辰大海吧'
>>> setattr(a,'y','你所访问的属性不在地球人的认知中，骚年，去征服星辰大海吧')
>>> setattr(a,'y')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    setattr(a,'y')
TypeError: setattr expected 3 arguments, got 2
>>> setattr(a,'y','琪宝宝')
>>> getattr(a,''y)
SyntaxError: invalid syntax
>>> getattr(a,'y')
'琪宝宝'
>>> delattr(a,'y')
>>> getattr(a,'y')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    getattr(a,'y')
AttributeError: 'A' object has no attribute 'y'
>>> 
