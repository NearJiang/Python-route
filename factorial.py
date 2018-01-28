def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
text = int(input('输入一个数字'))
print('%d的阶乘=%d'%(text,factorial(text)))
input('press[enter]')
