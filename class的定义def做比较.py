Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class dorm:
	def __init__(self,name):
		self.name=name
	def kick(self):
		print('%s电脑炸了' % self.name)

		
>>> a=dorm('大个')
>>> a.kick
<bound method dorm.kick of <__main__.dorm object at 0x034FA470>>
>>> a.kick()
大个电脑炸了
>>> b=dorm()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b=dorm()
TypeError: __init__() missing 1 required positional argument: 'name'
>>> 
