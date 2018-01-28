def months(n):
	while n<1:
		print('输入有误')
		return -1
	if n==1 or n==2:
		return 1
	else:
		return (months(n-1)+months(n-2))
question=int(input('你想知道第几个月的小兔子诞生量？：'))
print('%d月的小兔子诞生量为%d:'%(question,months(question)))
input('press[enter]')
