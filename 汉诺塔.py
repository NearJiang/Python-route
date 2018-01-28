def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从 x 移动到 y 上
        print(x,'-->',z)#将最低下的最后一个盘子从 x 移动到 z 上
        hanoi(n-1,y,x,z)#将 y 上的n-1个盘子移动到 z 上
n = int(input('输入汉诺塔的大金片数：'))
hanoi(n,'1','2','3')
input('press[enter]')
