Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mix = [1,2,3]
>>> mix
[1, 2, 3]
>>> mix.append('oooo')
>>> mix
[1, 2, 3, 'oooo']
>>> mix.append(['蒋爸爸，琪宝宝'])
>>> mix
[1, 2, 3, 'oooo', ['蒋爸爸，琪宝宝']]
>>> mix.extend(['蒋爸爸','琪宝宝'])
>>> mix
[1, 2, 3, 'oooo', ['蒋爸爸，琪宝宝'], '蒋爸爸', '琪宝宝']
>>> mix.insert（0，'特号蒋爸爸')
SyntaxError: invalid character in identifier
>>> mix.insert（0,'特号蒋爸爸')
SyntaxError: invalid character in identifier
>>> mix.insert(0,'特号蒋爸爸')
>>> mix
['特号蒋爸爸', 1, 2, 3, 'oooo', ['蒋爸爸，琪宝宝'], '蒋爸爸', '琪宝宝']
>>> 
