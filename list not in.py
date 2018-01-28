Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list = [12,56]
>>> list * 3
[12, 56, 12, 56, 12, 56]
>>> list *= 3
>>> list
[12, 56, 12, 56, 12, 56]
>>> list *= 3
>>> list
[12, 56, 12, 56, 12, 56, 12, 56, 12, 56, 12, 56, 12, 56, 12, 56, 12, 56]
>>> 12 in list
True
>>> '大波哥'not in list
True
>>> list1 = [1,['大波','oooo'],456]
>>> 大波 in list1
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    大波 in list1
NameError: name '大波' is not defined
>>> '大波' in list1
False
>>> '大波' in list1[1]
True
>>> 'oooo' in list[1][1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    'oooo' in list[1][1]
TypeError: 'int' object is not subscriptable
>>> list[1][1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list[1][1]
TypeError: 'int' object is not subscriptable
>>> list1[1][1]
'oooo'
>>> 'oooo' in list1[1][1]
True
>>> 
