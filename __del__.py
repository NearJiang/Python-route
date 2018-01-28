Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class C:
	def __init__(self):
		print('qibaobao')
	def __del__(self):
		print('琪宝宝')

		
>>> c1=C（）
SyntaxError: invalid character in identifier
>>> c1=C()
qibaobao
>>> del c1
琪宝宝
>>> 
