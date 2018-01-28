Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '[0] love [1] [2]'format('I','U',',qibaobao')
SyntaxError: invalid syntax
>>>  '[0] love [1] [2]'.format('I','U',',qibaobao')
 
SyntaxError: unexpected indent
>>> '[0] love [1] [2]'.format('I','U',',qibaobao')
'[0] love [1] [2]'
>>> '[0] love [1] [2]'.format('I','U',','qibaobao')
			  
SyntaxError: invalid syntax
>>> '{0} love {1} {2}'.format('I','U',',qibaobao')
'I love U ,qibaobao'
>>> '{a} love {b} {c}'.format(a='I',b='U',c=',qibaobao')
'I love U ,qibaobao'
>>> '{0} love {b} {c}'.format('I',b='U',c=',qibaobao')
'I love U ,qibaobao'
>>> 
