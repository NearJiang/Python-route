Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Parent:
	def yelling(self):
		print('啊妈，别叫了')

		
>>> class son(parent):
	pass

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    class son(parent):
NameError: name 'parent' is not defined
>>> class son(Parent):
	pass

>>> q=parent()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    q=parent()
NameError: name 'parent' is not defined
>>> q=Parent()
>>> q.yelling
<bound method Parent.yelling of <__main__.Parent object at 0x02EB0AD0>>
>>> q.yelling()
啊妈，别叫了
>>> p=son()
>>> p.yelling()
啊妈，别叫了
>>> 
