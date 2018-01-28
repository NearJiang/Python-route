Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class 儿子(list):   class DerivedClassName子类(BaseClassName父类)
	pass

>>> 孙子=儿子()
>>> 孙子.append(qibaobao)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    孙子.append(qibaobao)
NameError: name 'qibaobao' is not defined
>>> 孙子.append('小琪宝宝')
>>> 孙子.append(5)
>>> 孙子
['小琪宝宝', 5]
>>> 孙子.append(4)
>>> 孙子.append(8)
>>> 孙子
['小琪宝宝', 5, 4, 8]
>>> 孙子.sort()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    孙子.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> 孙子.remove('小琪宝宝')
>>> 孙子.sort()
>>> 孙子
[4, 5, 8]
>>> 
>>> class A:
	def q(self):
		print('saas')

		
>>> class B:
	def q(self):
		print('asasasasa')

		
>>> a=A()
>>> b=B()
>>> a.q()
saas
>>> b.q()
asasasasa
>>> 
