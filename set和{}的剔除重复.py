Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num={1,1,2,2,3,4,5,1,2,3,4}
>>> num
{1, 2, 3, 4, 5}
>>> set1=set([1,2,3,4,5,5,5,4,1])
>>> set1
{1, 2, 3, 4, 5}
>>> num1=[1,2,3,4,5,6,,5,2,3,0]
SyntaxError: invalid syntax
>>> num1=[1,2,3,4,5,6,5,2,3,0]
>>> temp = []
>>> for each in num1:
	if each not in []:
		each.append(temp)

		
Traceback (most recent call last):
  File "<pyshell#10>", line 3, in <module>
    each.append(temp)
AttributeError: 'int' object has no attribute 'append'
>>> for each in num1:
	if each not in temp:
		temp.append(each)

		
>>> temp
[1, 2, 3, 4, 5, 6, 0]
>>> num=list(set(num))
>>> num
[1, 2, 3, 4, 5]
>>> num1=list(set(num1))
>>> 
>>> num
[1, 2, 3, 4, 5]
>>> num1
[0, 1, 2, 3, 4, 5, 6]
>>> 
