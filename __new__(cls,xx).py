Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class q(str):
	def __new__(cls,word):
		word=word.upper()
		return str.__new__(cls,word)

	
>>> w=q()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    w=q()
TypeError: __new__() missing 1 required positional argument: 'word'
>>> w=q('I love qibaobao')
>>> w
'I LOVE QIBAOBAO'
>>> 
