Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def months(n):
	if n==1or2:
		return 1
	
SyntaxError: invalid syntax
>>> def months(n):
	if n==1 or 2:
		return 1
	else:
		return (n-1)+(n-1)

	
>>> months(20)
1
>>> def months(n):
	if n==1 or n==2:
		return 1
	else:
		return (n-1)+(n-1)

	
>>> months(20)
38
>>> def months(n):
	if n==1 or n==2:
		return 1
	else:
		return (months(n-1)+months(n-1))

	
>>> months(20)
262144
>>> def months(n):
	if n==1 or n==2:
		return 1
	else:
		return (months(n-1)+months(n-2))

	
>>> months(20)
6765
>>> def months(n):
	while n<1:
		print('输入有误')
		return -1
	if n==1 or n==2:
		return 1
	else:
		return (months(n-1)+months(n-2))

	
>>> months(0)
输入有误
-1
>>> 
