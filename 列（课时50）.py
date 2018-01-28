Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a={i:i%2==0 for i in range(10)}
>>> a
{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
>>>  0
 
SyntaxError: unexpected indent
>>> 0
0
>>> 1
1
>>> sum(i for i in range(100) if i %2)
2500
>>> 
