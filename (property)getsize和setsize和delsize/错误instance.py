Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class C:
	def __init__(self, size=10):
		self.size = size
	def getsize(self):
		return self.size
	def setsize(self, chicun):
		self.chicun = chicun
	def delsize(self):
		del self.size
	x=property(getsize, setsize, delsize)

	
>>> c1.x
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c1.x
NameError: name 'c1' is not defined
>>> c1=C()
>>> c1.x
10
>>> c1,x = 18
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c1,x = 18
TypeError: 'int' object is not iterable
>>> c1.x = 18
>>> c1.x
10
>>> c1.size
10
>>> 上面的setsize（self, chicun）：self.chicun = chicun，应该为self.size=chicun
