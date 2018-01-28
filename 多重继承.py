Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Base1:
	def foo1(self):
		print('我是foo1，我为Base1带盐')

		
>>> class Base2:
	def foo2(self):
		print('我是foo2，我为Base2带盐')

		
>>> class a(Base1, Base2):
	pass

>>> b=a()
>>> b.foo1()
我是foo1，我为Base1带盐
>>> b.foo2()
我是foo2，我为Base2带盐
>>> 
