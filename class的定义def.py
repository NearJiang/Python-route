Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  class dorm:
	def setname(self,name):
		self.name=name
	def kick(name):
		print('%s电脑炸了' % self.name)
		
SyntaxError: unexpected indent
>>> class dorm:
	def setname(self,name):
		self.name=name
	def kick(name):
		print('%s电脑炸了' % self.name)

		
>>> a=dorm()
>>> a.setname('大个')
>>> a.kick
<bound method dorm.kick of <__main__.dorm object at 0x034A14B0>>
>>> a.kick()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.kick()
  File "<pyshell#2>", line 5, in kick
    print('%s电脑炸了' % self.name)
NameError: name 'self' is not defined
>>> class dorm:
	def setname(self,name):
		self.name=name
	def kick(self):
		print('%s电脑炸了' % self.name)

		
>>> a=dorm()
>>> a.setname('大个')
>>> a.kick
<bound method dorm.kick of <__main__.dorm object at 0x034A1AF0>>
>>> a.kick()
大个电脑炸了
>>> 类（class）def 的时候 self 一定要放第一位
