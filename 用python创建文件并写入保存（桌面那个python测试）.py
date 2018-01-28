Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> q=open('C:\\Users\\Near\\Desktop\\pyhon测试.txt','w')
>>> q.wirte('我爱琪宝宝')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    q.wirte('我爱琪宝宝')
AttributeError: '_io.TextIOWrapper' object has no attribute 'wirte'

>>> q.write('我爱琪宝宝')
5
>>> q.close（）
SyntaxError: invalid character in identifier
>>> q.close()
>>> 
