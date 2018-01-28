Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> member = ['蒋爸爸','琪宝宝','xxx','yyy']
>>> member[0:2]
['蒋爸爸', '琪宝宝']
>>> member[0:3]
['蒋爸爸', '琪宝宝', 'xxx']
>>> member[1:4]
['琪宝宝', 'xxx', 'yyy']
>>> member[:3]
['蒋爸爸', '琪宝宝', 'xxx']
>>> member[0:]
['蒋爸爸', '琪宝宝', 'xxx', 'yyy']
>>> member[:]
['蒋爸爸', '琪宝宝', 'xxx', 'yyy']
>>> member 000 = member[:]
SyntaxError: invalid syntax
>>> member000 = member[:]
>>> member000
['蒋爸爸', '琪宝宝', 'xxx', 'yyy']
>>> 
