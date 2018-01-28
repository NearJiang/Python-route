Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str1 = 'daboge'
>>> str1.capitalize()
'Daboge'
>>> str2 = 'ASDF'
>>> str2.casefold()
'asdf'
>>> str2.center(50)
'                       ASDF                       '
>>> str2.count(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str2.count(a)
NameError: name 'a' is not defined
>>> str2.count(A)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str2.count(A)
NameError: name 'A' is not defined
>>> str2.count('A')
1
>>> str2.endswith('F')
True
>>> str2.endswith('DF')
True
>>> str3 = 'wo ai qi bao bao'
>>> str4 = 'wo\tai\tqi\tbao\tbao'
>>> str4.expandtabs()
'wo      ai      qi      bao     bao'
>>> str4.find('da')
-1
>>> str4.find('qi')
6
>>> str5 = 'O'
>>> str5.join("123')
	  
SyntaxError: EOL while scanning string literal
>>> str5.jion('123')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    str5.jion('123')
AttributeError: 'str' object has no attribute 'jion'
>>> str6 = 'OO'
>>> str6.join('123')
'1OO2OO3'
>>> str7 = 'I love U'
>>> str7.partiton('ov')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    str7.partiton('ov')
AttributeError: 'str' object has no attribute 'partiton'
>>> str7.partition('ov')
('I l', 'ov', 'e U')
>>> str7.replace('U','qibaobao')
'I love qibaobao'
>>> str7.split()
['I', 'love', 'U']
>>> str7.split('i')
['I love U']
>>> str7.split('l')
['I ', 'ove U']
>>> str7.translate(str.maketrans('v','oo'))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    str7.translate(str.maketrans('v','oo'))
ValueError: the first two maketrans arguments must have equal length
>>> str7
'I love U'
>>> str7.translate(str.maketrans('o','Q'))
'I lQve U'
>>> str7.zfill()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    str7.zfill()
TypeError: zfill() takes exactly 1 argument (0 given)
>>> str7.zfill(1)
'I love U'
>>> str7.zfill(2)
'I love U'
>>> str7.zfill(50)
'000000000000000000000000000000000000000000I love U'
>>> str7.zfill(10)
'00I love U'
>>> 
