Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> temp = (1,2,3,4,5)
>>> 2*temp
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
>>> temp = temp[2:]+('大波哥')+temp[:2]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    temp = temp[2:]+('大波哥')+temp[:2]
TypeError: can only concatenate tuple (not "str") to tuple
>>> temp = temp[2:] + ('大波哥') + temp[:2]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    temp = temp[2:] + ('大波哥') + temp[:2]
TypeError: can only concatenate tuple (not "str") to tuple
>>> temp = temp[:2]+('大波哥')+temp[2:]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    temp = temp[:2]+('大波哥')+temp[2:]
TypeError: can only concatenate tuple (not "str") to tuple
>>> temp = temp[:2] + ('大波哥') + temp[2:]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    temp = temp[:2] + ('大波哥') + temp[2:]
TypeError: can only concatenate tuple (not "str") to tuple
>>> temp = temp[:2]+('大波哥',)+temp[2:]
>>> temp
(1, 2, '大波哥', 3, 4, 5)
>>> 
