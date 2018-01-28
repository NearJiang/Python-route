Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class C:
	def __init__(self, size=10):
		self.size = size
	def getsize(self):
		return self.size
	def setsize(self, chicun):
		self.size = chicun
	def delsize(self):
		del self.size
	x=property(getsize, setsize, delsize)

	
>>> c1=C()
>>> c1.getsize()
10
>>> c1.x
10
>>> c1.x=18
>>> c1.x
18
>>> c1.size
18
>>> c1.getsize
<bound method C.getsize of <__main__.C object at 0x00657CF0>>
>>> c1.getsize()
18
>>> del c1.x
>>> c1.size
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    c1.size
AttributeError: 'C' object has no attribute 'size'
>>> 
