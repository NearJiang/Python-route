Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> string='琪宝宝'
>>> i=iter(string)
>>> next(i)
'琪'
>>> next(i)
'宝'
>>> next(i)
'宝'
>>> 
>>> string='琪宝宝'
>>> it=iter(string)
>>> while True:
	try:
		each=next(it)
	except StopIteration:
		break
	print(each)

	
琪
宝
宝
>>> 
