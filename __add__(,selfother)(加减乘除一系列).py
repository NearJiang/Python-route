Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class newint(int):
	def __add__(self,other):
		return int.__add__(self,other)
	def __sub__(self,other):
		return int.__sub__(self,other)

	
>>> a=newint(5)
>>> b+newint(8)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b+newint(8)
NameError: name 'b' is not defined
>>> b=newint(8)
>>> a+b
13
>>> a-b
-3
>>> b-a
3
>>> class newint(int):
	def __add__(self,other):
		return int(self)+int(other)
	def __sub__(self,other):
		return int(self)-int(other)

	
>>> a=newint(5)
>>> b=newint(8)
>>> a+b
13
>>> a-b
-3
>>> b-a
3
>>> ①add sub(subtract) ②mul(multiply) ③truediv(true divide 最正宗的除法，该等于什么就等于什么) ④floordiv(除下来只等于前面的整数，后面小数去掉)⑤mod（%）
SyntaxError: invalid character in identifier
>>> ⑥divmod(divide,mod 表现形式为（a//b,a%b）)
