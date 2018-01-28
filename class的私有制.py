Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class person:
	name="大波"

	
>>> 去、
SyntaxError: invalid character in identifier
>>> q=person()
>>> q.name
'大波'
>>> class person:
	__name="大波"

	
>>> q.person()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    q.person()
AttributeError: 'person' object has no attribute 'person'
>>> q=person()
>>> q.__name
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    q.__name
AttributeError: 'person' object has no attribute '__name'
>>> class person:
	__name="大波"
	def getname(self):
		return self.name

	
>>> q=person
>>> q.getname()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    q.getname()
TypeError: getname() missing 1 required positional argument: 'self'
>>> q=person()
>>> q.getname()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    q.getname()
  File "<pyshell#14>", line 4, in getname
    return self.name
AttributeError: 'person' object has no attribute 'name'
>>> class person:
	__name="大波"
	def getname(self):
		return self.__name

	
>>> q=person()
>>> q.getname()
'大波'
>>> q._person__name
'大波'
>>> '__'名为私有，但也是伪私有，_xxx__变量name即可跳出
