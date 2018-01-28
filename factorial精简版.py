def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
text = int(input('输入一个数:'))
print('%d的阶乘=%d'%(text,factorial(text)))
input('press[enter]')
