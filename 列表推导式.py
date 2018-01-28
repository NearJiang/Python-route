Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=[i for i range(100) if not (i%2)and(i%3)]
SyntaxError: invalid syntax
>>> a=[i for i in range(100) if not (i%2)and(i%3)]
>>> a
[2, 4, 8, 10, 14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, 56, 58, 62, 64, 68, 70, 74, 76, 80, 82, 86, 88, 92, 94, 98]
>>> a=[i for i in range(100) if not (i%2)and i%3]
>>> a
[2, 4, 8, 10, 14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, 56, 58, 62, 64, 68, 70, 74, 76, 80, 82, 86, 88, 92, 94, 98]
>>> 2%2
0
>>> #if not i %2    单独在句子中写i%2就是说这个为True，就是说i%2=1，也就是说i是
>>> #也就是说i是不能整除2的
>>> #if not i%2  就是说如果i%2不成立的情况，也就是等于0的情况，也就是所有2的所有倍数
>>> #if not i%2 and i%3 就是说i是2的倍数，但不能是3的倍数
